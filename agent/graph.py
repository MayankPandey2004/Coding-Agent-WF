from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from langgraph.checkpoint.memory import MemorySaver

from agent.state import AgentState
from agent.tools import ALL_TOOLS
from agent.nodes import (
    planner_node,
    coder_node,
    evaluator_node,
    should_continue,
    route_after_eval,
)


def build_graph():
    graph = StateGraph(AgentState)

    graph.add_node("planner", planner_node)
    graph.add_node("coder", coder_node)
    graph.add_node("tools", ToolNode(ALL_TOOLS))
    graph.add_node("evaluator", evaluator_node)

    graph.add_edge(START, "planner")
    graph.add_edge("planner", "coder")

    graph.add_conditional_edges(
        "coder", should_continue, {"tools": "tools", "evaluate": "evaluator"}
    )
    graph.add_edge("tools", "coder")

    graph.add_conditional_edges(
        "evaluator", route_after_eval, {"retry": "coder", "end": END}
    )

    checkpointer = MemorySaver()
    return graph.compile(checkpointer=checkpointer)
