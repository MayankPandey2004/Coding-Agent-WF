import uuid
from dotenv import load_dotenv

load_dotenv()

from agent.graph import build_graph

def main():
    app = build_graph()
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    print("Coding Agent (type 'exit' to quit)")
    while True:
        task = input("\nTask: ").strip()
        if task.lower() in ("exit", "quit"):
            break

        result = app.invoke({"task": task}, config=config)

        print("\n--- Final status:", result.get("status"), "---")
        last_ai = [m for m in result["messages"] if m.type == "ai"]
        if last_ai:
            print(last_ai[-1].content)

if __name__ == "__main__":
    main()
