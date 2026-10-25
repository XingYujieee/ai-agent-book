"""Restore selected saved evidence to its exact Git bytes after CRLF checkout.

Writes only when CRLF-to-LF conversion alone explains the entire difference.
No expected hash, semantic content, or locally edited file is changed.
"""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PREFIXES = {
    6: ["chapter6/xlerobot-teleoperation/validation/runs/local-gpu/", "chapter6/gemini-xlerobot-navigation/validation/runs/local-gpu/", "chapter6/rgb-sim2real-grasping/validation/runs/local-gpu/", "chapter6/streaming-speech/"],
    7: ["chapter7/user-memory-policy-eval/"],
    10: ["chapter10/autonomous-phone-registration/"],
}
paths = subprocess.check_output(["git", "ls-files"], cwd=ROOT, text=True).splitlines()
for chapter, prefixes in PREFIXES.items():
    report = ROOT / "personal-learning" / f"task{chapter}" / "results" / "eol-restoration.json"
    restored = json.loads(report.read_text(encoding="utf-8"))["files"] if report.exists() else []
    before = len(restored)
    for name in paths:
        if not any(name.startswith(p) for p in prefixes) or Path(name).suffix not in (".json", ".py", ".md", ".txt", ".jsonl"):
            continue
        path = ROOT / name
        if not path.is_file():
            continue
        current = path.read_bytes()
        original = subprocess.check_output(["git", "show", f"faa6db95:{name}"], cwd=ROOT)
        if current != original and current.replace(b"\r\n", b"\n") == original:
            path.write_bytes(original)
            restored.append({"path": name, "git_sha256": hashlib.sha256(original).hexdigest()})
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps({"reason": "Windows checkout CRLF conversion only", "files": restored}, indent=2)+"\n", encoding="utf-8")
    print(f"Chapter {chapter}: restored exact Git bytes in {len(restored)-before} more files")
