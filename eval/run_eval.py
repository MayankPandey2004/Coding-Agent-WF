import json
import os
import time
import uuid
import shutil
from dotenv import load_dotenv

load_dotenv()

from agent.graph import build_graph
from eval.grader import setup_eval_sandbox, grade_task

DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset", "tasks.json")


def run_eval():
    with open(DATASET_PATH) as f:
        tasks = json.load(f)

    setup_eval_sandbox()

    app = build_graph()
    results = []

    print(f"Running eval suite: {len(tasks)} tasks\n")

    for task in tasks:
        print(f"--- {task['id']} ---")
        thread_id = str(uuid.uuid4())
        config = {"configurable": {"thread_id": thread_id}}

        start = time.time()
        tool_call_count = 0
        try:
            for step in app.stream(
                {"task": task["prompt"]}, config=config, stream_mode="updates"
            ):
                for node_name, node_output in step.items():
                    if node_name == "coder":
                        ai_msg = node_output["messages"][-1]
                        tool_call_count += len(getattr(ai_msg, "tool_calls", []) or [])
        except Exception as e:
            print(f"  Agent run failed: {e}")
            results.append({
                "id": task["id"],
                "passed": False,
                "reason": f"agent crash: {e}",
                "attempts": None,
                "tool_calls": tool_call_count,
                "duration_sec": round(time.time() - start, 1),
            })
            continue

        duration = round(time.time() - start, 1)
        final_state = app.get_state(config).values
        attempts = final_state.get("attempt_count")

        grade = grade_task(task)
        grade["attempts"] = attempts
        grade["tool_calls"] = tool_call_count
        grade["duration_sec"] = duration
        results.append(grade)

        status = "PASS" if grade["passed"] else "FAIL"
        print(f"  {status} | attempts={attempts} | tool_calls={tool_call_count} | {duration}s")
        if not grade["passed"]:
            print(f"  Reason: {grade['reason'][:200]}")
        print()

    print_report(results)
    return results


def print_report(results):
    total = len(results)
    passed = sum(1 for r in results if r["passed"])
    avg_attempts = sum(r["attempts"] or 0 for r in results) / total if total else 0
    avg_tool_calls = sum(r["tool_calls"] for r in results) / total if total else 0
    avg_duration = sum(r["duration_sec"] for r in results) / total if total else 0

    print("=" * 50)
    print(f"EVAL REPORT: {passed}/{total} tasks passed ({round(100*passed/total, 1)}%)")
    print(f"Avg attempts: {round(avg_attempts, 2)}")
    print(f"Avg tool calls: {round(avg_tool_calls, 2)}")
    print(f"Avg duration: {round(avg_duration, 2)}s")
    print("=" * 50)
    for r in results:
        status = "✅" if r["passed"] else "❌"
        print(f"  {status} {r['id']}")


if __name__ == "__main__":
    run_eval()
