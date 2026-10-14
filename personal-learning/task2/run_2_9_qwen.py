"""Run a small, read-only Chapter 2.9 comparison with an existing DashScope key.

Run from the repository root with DASHSCOPE_API_KEY and DASHSCOPE_BASE_URL set.
The key is read from the environment and is never written to output.
"""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PROJECT = ROOT / "chapter2" / "system-hint"
OUTPUT = Path(__file__).resolve().parent / "results"
sys.path.insert(0, str(PROJECT))

from agent import SystemHintAgent, SystemHintConfig  # noqa: E402


def main() -> None:
    key = os.environ.get("DASHSCOPE_API_KEY")
    if not key:
        raise SystemExit("DASHSCOPE_API_KEY is required")
    OUTPUT.mkdir(parents=True, exist_ok=True)
    os.chdir(PROJECT)
    task = (
        "Use only read_file to read the first 3 lines of README.md. "
        "Quote its first heading exactly, then give a final answer. "
        "Do not change or create any project file."
    )
    summary = {"experiment_id": "2-9-equivalent", "provider": "dashscope", "model": "qwen3.7-plus", "task": task, "arms": {}}
    for name, enabled in (("disabled", False), ("full", True)):
        trace = OUTPUT / f"2-9-{name}-trajectory.json"
        config = SystemHintConfig(
            enable_timestamps=enabled,
            enable_tool_counter=enabled,
            enable_todo_list=enabled,
            enable_detailed_errors=enabled,
            enable_system_state=enabled,
            save_trajectory=True,
            trajectory_file=str(trace),
        )
        agent = SystemHintAgent(key, provider="dashscope", model="qwen3.7-plus", config=config, verbose=False)
        result = agent.execute_task(task, max_iterations=5)
        summary["arms"][name] = {
            "success": result.get("success"),
            "final_answer": result.get("final_answer"),
            "trajectory_file": trace.name,
            "tool_calls": len(agent.tool_calls),
        }
        print(name, summary["arms"][name]["success"], summary["arms"][name]["tool_calls"])
    (OUTPUT / "2-9-qwen-comparison.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
