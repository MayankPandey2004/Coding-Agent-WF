from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import json
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

print(f"Looking for agent module at: {ROOT}")
print(f"Agent dir exists: {(ROOT / 'agent').exists()}")

try:
    from agent.graph import build_graph
    print("Agent imported successfully")
except ImportError as e:
    print(f"Error: {e}")
    print(f"sys.path: {sys.path}")
    raise

app = FastAPI(title="CodeSmith Agent API")


class TaskRequest(BaseModel):
    task: str
    thread_id: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/agent/stream")
async def stream_agent(request: TaskRequest):
    def generate():
        try:
            agent = build_graph()
            config = {"configurable": {"thread_id": request.thread_id}}

            for step in agent.stream({"task": request.task}, config=config, stream_mode="updates"):
                for node_name, node_output in step.items():
                    if node_name in ["planner", "coder", "executor", "evaluator"]:
                        yield f"data: {json.dumps({'node': node_name})}\n\n"

            final_state = agent.get_state(config).values
            yield f"data: {json.dumps({'passed': final_state.get('passed', False)})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    print("Starting on http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)
