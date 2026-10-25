"""Run the explicitly offline teaching paths; keep commands and output together."""
import concurrent.futures
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
def output(chapter, name):
    return str(ROOT / "personal-learning" / f"task{chapter}" / "results" / name)

JOBS = [
    (5, "logic-solver", "chapter5/code-for-logic", ["demo.py", "--mode", "solver", "--output", output(5,"logic-solver.json")]),
    (5, "log-parser", "chapter5/adaptive-log-parser", ["demo.py", "--offline", "--output", output(5,"parsed-logs.jsonl")]),
    (5, "dynamic-form", "chapter5/dynamic-form", ["demo.py", "--offline", "--output", output(5,"flight-form.html")]),
    (5, "video-smoke", "chapter5/video-edit", ["demo.py", "--smoke", "--output", output(5,"edit-smoke.mp4")]),
    (6, "event-timer", "chapter6/agent-with-event-trigger", ["event_loop_demo.py", "--mock", "--trigger", "timer", "--duration", "2", "--delay", "0.2"]),
    (6, "async-demo", "chapter6/async-agent", ["demo.py", "offline"]),
    (7, "cost-analysis", "chapter7/agent-cost-analysis", ["demo.py", "--offline", "--scenario", "all", "--output", output(7,"cost-analysis.json")]),
    (8, "dpo-mock", "chapter8/premature-completion-dpo", ["demo.py"]),
    (9, "trajectory-verifier", "chapter9/trajectory-verifier", ["demo.py"]),
    (9, "prompt-plan", "chapter9/prompt-auto-optimization", ["demo.py", "--dry-run"]),
    (9, "rpa-replay", "chapter9/browser-use-rpa", ["workflow_validation_demo.py"]),
    (9, "safety-gate", "chapter9/harness-safety-gate", ["run_experiment_9_7.py", "--quick"]),
    (9, "evolution-reference", "chapter9/self-evolution-eval", ["demo.py", "--profile", "all", "--output", output(9,"reference-evolution.json")]),
    (10, "roles-list", "chapter10/multi-role-transfer", ["demo.py", "--list-roles"]),
    (10, "translation-plan", "chapter10/book-translation", ["demo.py", "--dry-run", "--out-dir", output(10,"translation-plan")]),
    (10, "werewolf-offline", "chapter10/voice-werewolf", ["demo.py", "--offline", "--seed", "42", "--report", output(10,"werewolf-offline.json")]),
]
def run(job):
    chapter,name,cwd,args=job
    target=Path(output(chapter,"demos")); target.mkdir(parents=True,exist_ok=True)
    env=os.environ.copy(); env.update(PYTHONIOENCODING="utf-8",PYTHONUTF8="1",FLUX_TICK_REAL="0.005")
    start=time.monotonic()
    try:
        result=subprocess.run([sys.executable,*args],cwd=ROOT/cwd,env=env,capture_output=True,timeout=120)
        code=result.returncode; raw=result.stdout+result.stderr
    except subprocess.TimeoutExpired as error:
        code=None;raw=(error.stdout or b"")+(error.stderr or b"")
    (target/f"{name}.txt").write_bytes(raw)
    meta={"name":name,"mode":"offline_mechanism_or_saved_data_reanalysis","formal_experiment_completed":False,
          "command":["python",*args],"cwd":cwd,"returncode":code,"seconds":round(time.monotonic()-start,3),"log":f"{name}.txt"}
    (target/f"{name}.json").write_text(json.dumps(meta,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"{chapter}/{name}: exit={code}",flush=True)

if __name__=="__main__":
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(run,JOBS))
