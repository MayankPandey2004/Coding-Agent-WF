import os
from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict, Annotated, Sequence
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq


class MinimalState(TypedDict):
    messages: Annotated[Sequence[BaseMessage], add_messages]


llm = ChatGroq(model="openai/gpt-oss-120b", api_key=os.environ["GROQ_API_KEY"])


def coder_node(state: MinimalState) -> dict:
    response = llm.invoke(state["messages"])
    return {"messages": [response]}


graph = StateGraph(MinimalState)
graph.add_node("coder", coder_node)
graph.add_edge(START, "coder")
graph.add_edge("coder", END)
app = graph.compile()


if __name__ == "__main__":
    result = app.invoke(
        {"messages": [HumanMessage(content="Write a Python function that adds two numbers.")]}
    )
    print("\n--- Agent response ---\n")
    print(result["messages"][-1].content)
