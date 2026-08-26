import uuid
from dotenv import load_dotenv

load_dotenv()

from agent.graph import build_graph
from memory.store import save_memory

def main():
    app = build_graph()
    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}

    print("Coding Agent (type 'exit' to quit)")
    while True:
        task = input("\nTask: ").strip()
        if task.lower() in ("exit", "quit"):
            break
        if not task:
            continue

        result = app.invoke({"task": task}, config=config)

        print("\n--- Final status:", result.get("status"), "| attempts:", result.get("attempt_count"), "---")
        last_ai = [m for m in result["messages"] if m.type == "ai"]
        if last_ai:
            print(last_ai[-1].content)
            summary = f"Task: {task}\nOutcome ({result.get('status')}): {last_ai[-1].content[:300]}"
            save_memory(summary)

if __name__ == "__main__":
    main()
