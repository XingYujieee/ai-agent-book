"""Read-only audit of the chapter's saved validation manifests.

Run from the repository root with: python personal-learning/task3/verify_history.py
The author workstation paths in latest.json are mapped to this checkout only
when they contain the ai-agent-book repository segment.
"""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CHAPTER = ROOT / "chapter3"
OUTPUT = ROOT / "personal-learning" / "task3" / "results" / "historical-evidence-audit.json"
BASELINE_REF = "6ccf611d"  # fork main before this Chapter 3 work


def committed_bytes(path: Path) -> bytes | None:
    """Read the baseline Git blob, avoiding Windows checkout CRLF conversion."""
    try:
        relative = path.relative_to(ROOT).as_posix()
    except ValueError:
        return None
    process = subprocess.run(
        ["git", "show", f"{BASELINE_REF}:{relative}"], cwd=ROOT, capture_output=True, check=False
    )
    return process.stdout if process.returncode == 0 else None


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def local_input(raw: str) -> Path | None:
    normalized = raw.replace("\\", "/")
    marker = "/ai-agent-book/"
    if marker not in normalized:
        return None
    return ROOT / normalized.split(marker, 1)[1]


def main() -> None:
    rows = []
    for latest in sorted(CHAPTER.glob("*/validation/latest.json")):
        pointer_blob = committed_bytes(latest)
        if pointer_blob is None:
            raise RuntimeError(f"No committed latest.json: {latest}")
        pointer = json.loads(pointer_blob.decode("utf-8"))
        run_dir = latest.parent / "runs" / pointer["run_id"]
        artifacts = {}
        for name, expected in pointer.get("artifacts", {}).items():
            path = run_dir / name
            blob = committed_bytes(path)
            artifacts[name] = {
                "committed": blob is not None,
                "sha256_matches": blob is not None and digest(blob) == expected,
            }

        inputs = {"matched": 0, "mismatched": 0, "missing": 0, "external": 0}
        input_exceptions = []
        for item in pointer.get("inputs", []):
            path = local_input(item["path"])
            if path is None:
                inputs["external"] += 1
                input_exceptions.append({"path": item["path"], "reason": "outside checkout"})
            elif (blob := committed_bytes(path)) is None:
                inputs["missing"] += 1
                input_exceptions.append({"path": str(path.relative_to(ROOT)), "reason": "missing"})
            elif digest(blob) != item["sha256"]:
                inputs["mismatched"] += 1
                input_exceptions.append({"path": str(path.relative_to(ROOT)), "reason": "hash differs"})
            else:
                inputs["matched"] += 1

        evidence_blob = committed_bytes(run_dir / "evidence.json")
        evidence = json.loads(evidence_blob.decode("utf-8")) if evidence_blob else {}
        acceptance = evidence.get("acceptance", {})
        rows.append(
            {
                "experiment": pointer["experiment"],
                "project": latest.parent.parent.name,
                "author_status": pointer["status"],
                "run_id": pointer["run_id"],
                "artifacts": artifacts,
                "inputs": inputs,
                "input_exceptions": input_exceptions,
                "acceptance_false": [key for key, value in acceptance.items() if value is False],
                "summary": evidence.get("summary", {}),
            }
        )

    report = {
        "scope": "Read-only SHA-256 audit of baseline Git blobs; no historical experiment was rerun. Working-tree CRLF bytes are intentionally excluded.",
        "baseline_ref": BASELINE_REF,
        "latest_files": len(rows),
        "author_passed": sum(row["author_status"] == "passed" for row in rows),
        "artifact_hashes_matched": sum(
            item["sha256_matches"] for row in rows for item in row["artifacts"].values()
        ),
        "artifact_hashes_total": sum(len(row["artifacts"]) for row in rows),
        "input_totals": {
            key: sum(row["inputs"][key] for row in rows)
            for key in ("matched", "mismatched", "missing", "external")
        },
        "rows": rows,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"historical files={report['latest_files']}, artifact hashes "
        f"{report['artifact_hashes_matched']}/{report['artifact_hashes_total']}, "
        f"inputs={report['input_totals']}"
    )


if __name__ == "__main__":
    main()
