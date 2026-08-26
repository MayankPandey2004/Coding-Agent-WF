import os
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from agent.state import AgentState
from agent.tools import ALL_TOOLS
from memory.store import retrieve_memories

llm = ChatGroq(model="openai/gpt-oss-120b", api_key=os.environ["GROQ_API_KEY"])
llm_with_tools = llm.bind_tools(ALL_TOOLS)

CODER_SYSTEM_PROMPT = """You are a coding agent. You write code, save it with write_file,
then run it with run_bash or run_tests to verify it works. If something fails, read the
error and fix the code. Always use the provided tools rather than just describing what
you would do.

For any task with more than one step, call todo_write first with a list of the steps
you plan to take. As you complete each step, call todo_complete with its index. Use
todo_read if you need to check what's left to do. For simple one-step tasks, you can
skip the todo list.

If the task involves a Figma design (mentions a file key, node ID, or "figma"), use
read_figma_file to see the overall structure first, then get_figma_node on the specific
frame to get exact colors, fonts, sizes, and spacing. Use those exact values when
generating matching HTML/CSS or React code - don't guess or approximate."""


def planner_node(state: AgentState) -> dict:
    is_first_ever = state.get("attempt_count") is None
    messages = []
    if is_first_ever:
        memories = retrieve_memories(state["task"], k=3)
        prompt = CODER_SYSTEM_PROMPT
        if memories:
            memory_text = "\n".join(f"- {m}" for m in memories)
            prompt += f"\n\nRelevant context from past sessions:\n{memory_text}"
        messages.append(SystemMessage(content=prompt))
    messages.append(HumanMessage(content=state["task"]))
    return {
        "messages": messages,
        "attempt_count": 0,
        "max_retries": state.get("max_retries", 3),
        "status": "in_progress",
    }


def coder_node(state: AgentState) -> dict:
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


def evaluator_node(state: AgentState) -> dict:
    last_msgs = state["messages"][-6:]
    tool_outputs = [m.content for m in last_msgs if m.type == "tool"]
    combined_output = "\n".join(tool_outputs).lower()

    failed = any(
        kw in combined_output for kw in ["error", "traceback", "failed", "exception"]
    )
    status = "fail" if failed else "pass"

    return {
        "test_results": "\n".join(tool_outputs),
        "status": status,
        "attempt_count": state["attempt_count"] + 1,
    }


def should_continue(state: AgentState) -> str:
    last_message = state["messages"][-1]
    if getattr(last_message, "tool_calls", None):
        return "tools"
    return "evaluate"


def route_after_eval(state: AgentState) -> str:
    if state["status"] == "pass":
        return "end"
    if state["attempt_count"] >= state["max_retries"]:
        return "end"
    return "retry"
