import os
import shutil
import subprocess

EVAL_SANDBOX = os.path.abspath("./eval_sandbox")


def setup_eval_sandbox():
    if os.path.exists(EVAL_SANDBOX):
        shutil.rmtree(EVAL_SANDBOX)
    os.makedirs(EVAL_SANDBOX)


def grade_task(task: dict) -> dict:
    """Copy the expected file from the real sandbox, run the test_snippet against
    it, and return a pass/fail result with details."""
    source_file = os.path.join(os.path.abspath("./sandbox"), task["expected_file"])
    result = {
        "id": task["id"],
        "passed": False,
        "reason": "",
    }

    if not os.path.exists(source_file):
        result["reason"] = f"Expected file {task['expected_file']} was not created"
        return result

    dest_file = os.path.join(EVAL_SANDBOX, task["expected_file"])
    shutil.copy(source_file, dest_file)

    test_file = os.path.join(EVAL_SANDBOX, f"test_{task['id']}.py")
    with open(test_file, "w") as f:
        f.write(task["test_snippet"])

    proc = subprocess.run(
        ["pytest", test_file, "-q"],
        cwd=EVAL_SANDBOX,
        capture_output=True,
        text=True,
        timeout=30,
    )

    output = proc.stdout + proc.stderr
    result["passed"] = proc.returncode == 0
    result["reason"] = output.strip()[-500:]
    return result
