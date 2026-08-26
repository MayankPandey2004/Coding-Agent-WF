import subprocess
import os
import json
import requests
from langchain_core.tools import tool

WORKDIR = os.path.abspath("./sandbox")
os.makedirs(WORKDIR, exist_ok=True)


def _safe_path(path: str) -> str:
    full = os.path.abspath(os.path.join(WORKDIR, path))
    if not full.startswith(WORKDIR):
        raise ValueError("Path escapes sandbox directory.")
    return full


@tool
def read_file(path: str) -> str:
    """Read the contents of a file inside the sandbox directory."""
    try:
        with open(_safe_path(path), "r") as f:
            return f.read()
    except Exception as e:
        return f"ERROR reading file: {e}"


@tool
def write_file(path: str, content: str) -> str:
    """Write content to a file inside the sandbox directory. Overwrites if it exists."""
    try:
        full = _safe_path(path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w") as f:
            f.write(content)
        return f"Wrote {len(content)} chars to {path}"
    except Exception as e:
        return f"ERROR writing file: {e}"


@tool
def list_directory(path: str = ".") -> str:
    """List files and folders inside a directory in the sandbox."""
    try:
        target = _safe_path(path)
        return "\n".join(os.listdir(target))
    except Exception as e:
        return f"ERROR listing directory: {e}"


@tool
def run_bash(command: str, timeout: int = 30) -> str:
    """Run a shell command inside the sandbox directory. Use for running scripts or tests."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=WORKDIR,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        output = result.stdout + result.stderr
        return output.strip() or "(no output)"
    except subprocess.TimeoutExpired:
        return "ERROR: command timed out"
    except Exception as e:
        return f"ERROR running command: {e}"


@tool
def run_tests(test_path: str = ".") -> str:
    """Run pytest on the given path inside the sandbox and return the results."""
    return run_bash.invoke({"command": f"pytest {test_path} -q", "timeout": 30})


_TODO_LIST = []


@tool
def todo_write(items: list[str]) -> str:
    """Set or replace the current todo list with a list of step descriptions.
    Call this at the start of a multi-step task to plan out the work."""
    global _TODO_LIST
    _TODO_LIST = [{"text": item, "done": False} for item in items]
    return f"Todo list set with {len(items)} items."


@tool
def todo_read() -> str:
    """Read the current todo list and its completion status."""
    if not _TODO_LIST:
        return "No todo items set."
    lines = []
    for i, item in enumerate(_TODO_LIST):
        mark = "[x]" if item["done"] else "[ ]"
        lines.append(f"{i}. {mark} {item['text']}")
    return "\n".join(lines)


@tool
def todo_complete(index: int) -> str:
    """Mark the todo item at the given index (0-based) as complete."""
    global _TODO_LIST
    if 0 <= index < len(_TODO_LIST):
        _TODO_LIST[index]["done"] = True
        return f"Marked item {index} as complete."
    return f"ERROR: no todo item at index {index}"


FIGMA_TOKEN = os.environ.get("FIGMA_TOKEN")
FIGMA_API_BASE = "https://api.figma.com/v1"


@tool
def read_figma_file(file_key: str) -> str:
    """Fetch the full node tree of a Figma file given its file key. Returns a
    trimmed JSON summary of top-level structure."""
    try:
        resp = requests.get(
            f"{FIGMA_API_BASE}/files/{file_key}",
            headers={"X-Figma-Token": FIGMA_TOKEN},
        )
        if resp.status_code != 200:
            return f"ERROR: Figma API returned {resp.status_code}: {resp.text[:300]}"
        data = resp.json()

        def summarize(node, depth=0):
            indent = "  " * depth
            line = f"{indent}- {node.get('name')} ({node.get('type')}) id={node.get('id')}"
            lines = [line]
            for child in node.get("children", [])[:10]:
                lines.extend(summarize(child, depth + 1))
            return lines

        tree = "\n".join(summarize(data["document"]))
        return tree[:3000]
    except Exception as e:
        return f"ERROR reading Figma file: {e}"


@tool
def get_figma_node(file_key: str, node_id: str) -> str:
    """Fetch detailed design properties (fills, typography, spacing, layout)
    for a specific node in a Figma file, given the file key and node ID
    (e.g. '3:4')."""
    try:
        resp = requests.get(
            f"{FIGMA_API_BASE}/files/{file_key}/nodes",
            headers={"X-Figma-Token": FIGMA_TOKEN},
            params={"ids": node_id},
        )
        if resp.status_code != 200:
            return f"ERROR: Figma API returned {resp.status_code}: {resp.text[:300]}"
        data = resp.json()
        return json.dumps(data, indent=2)[:4000]
    except Exception as e:
        return f"ERROR reading Figma node: {e}"


ALL_TOOLS = [
    read_file,
    write_file,
    list_directory,
    run_bash,
    run_tests,
    todo_write,
    todo_read,
    todo_complete,
    read_figma_file,
    get_figma_node,
]
