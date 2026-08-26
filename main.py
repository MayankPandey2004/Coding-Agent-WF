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

        result = None
        rate_limited = False
        try:
            for step in app.stream({"task": task}, config=config, stream_mode="updates"):
                for node_name, node_output in step.items():
                    if node_name == "coder":
                        ai_msg = node_output["messages"][-1]
                        for tc in getattr(ai_msg, "tool_calls", []) or []:
                            print(f"  [tool call] {tc['name']}({tc['args']})")
                    result = node_output
        except Exception as e:
            if "rate_limit" in str(e).lower() or "429" in str(e):
                print("\n⚠️  Rate limit reached on the LLM provider. Please wait a few minutes and try again.")
                rate_limited = True
            else:
                raise

        if rate_limited:
            continue

        final_state = app.get_state(config).values
        print("\n--- Final status:", final_state.get("status"), "| attempts:", final_state.get("attempt_count"), "---")
        def extract_text(msg_content):
            if isinstance(msg_content, str):
                return msg_content
            if isinstance(msg_content, list):
                parts = []
                for block in msg_content:
                    if isinstance(block, dict) and block.get("type") == "text":
                        parts.append(block.get("text", ""))
                    elif isinstance(block, str):
                        parts.append(block)
                return "\n".join(parts)
            return str(msg_content)

        last_ai = [m for m in final_state["messages"] if m.type == "ai"]
        if last_ai:
            clean_text = extract_text(last_ai[-1].content)
            print(clean_text)
            summary = f"Task: {task}\nOutcome ({final_state.get('status')}): {clean_text[:300]}"
            save_memory(summary)

if __name__ == "__main__":
    main()
