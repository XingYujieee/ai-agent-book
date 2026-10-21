"""Audit the five Chapter 4 canonical manifests against committed Git blobs."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASELINE_REF = "382d39d2"
LEDGER = ROOT / "chapter4" / "EXPERIMENT_LEDGER.md"
OUTPUT = ROOT / "personal-learning" / "task4" / "results" / "historical-evidence-audit.json"


def blob(path: Path) -> bytes | None:
    relative = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{BASELINE_REF}:{relative}"],
        cwd=ROOT,
        capture_output=True,
        check=False,
    )
    return result.stdout if result.returncode == 0 else None


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    ledger_blob = blob(LEDGER)
    if ledger_blob is None:
        raise RuntimeError("Baseline ledger unavailable")
    ledger = ledger_blob.decode("utf-8")
    rows = []
    pattern = r"\| (4-[1-5]) \| `([^`]+)` \| (passed|blocked) \| (true|false) \| `([0-9a-f]{64})` \|"
    for experiment, relative_dir, status, complete, expected in re.findall(pattern, ledger):
        run_dir = ROOT / "chapter4" / relative_dir
        manifest_blob = blob(run_dir / "manifest.json")
        if manifest_blob is None:
            raise RuntimeError(f"Missing committed manifest: {run_dir}")
        manifest = json.loads(manifest_blob)
        items = manifest.get("files")
        if items is None:
            items = [
                {"path": name, "sha256": value}
                for name, value in manifest.get("artifacts", {}).items()
            ]
        file_checks = []
        for item in items:
            source = blob(run_dir / item["path"])
            file_checks.append(
                {
                    "path": item["path"],
                    "committed": source is not None,
                    "sha256_matches": source is not None and sha(source) == item["sha256"],
                    "bytes_match": source is not None
                    and ("bytes" not in item or len(source) == item["bytes"]),
                }
            )
        summary_blob = blob(run_dir / "summary.json") or blob(run_dir / "evidence.json")
        summary = json.loads(summary_blob) if summary_blob else {}
        rows.append(
            {
                "experiment": experiment,
                "canonical_run": relative_dir,
                "ledger_status": status,
                "ledger_official_complete": complete == "true",
                "manifest_sha256_matches": sha(manifest_blob) == expected,
                "manifest_recorded_experiment": manifest.get("experiment"),
                "file_checks": file_checks,
                "summary": summary.get("summary", summary),
            }
        )
    report = {
        "scope": "Read-only audit of historical Git blobs; no external provider calls were repeated.",
        "baseline_ref": BASELINE_REF,
        "canonical_runs": len(rows),
        "manifest_hashes_matched": sum(x["manifest_sha256_matches"] for x in rows),
        "files_total": sum(len(x["file_checks"]) for x in rows),
        "file_hashes_matched": sum(
            check["sha256_matches"] for row in rows for check in row["file_checks"]
        ),
        "rows": rows,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(
        f"manifests {report['manifest_hashes_matched']}/{report['canonical_runs']}; "
        f"files {report['file_hashes_matched']}/{report['files_total']}"
    )


if __name__ == "__main__":
    main()
