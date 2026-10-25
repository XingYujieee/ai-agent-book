"""Inventory manuscript experiments and inspect a bounded sample of saved evidence.

The baseline is immutable. Missing files and stale hashes stay visible; neither
the ledger's claim nor a hash match is treated as a new external experiment.
"""
from __future__ import annotations

import hashlib
import json
import posixpath
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = "faa6db95"
TRACKED = set(subprocess.check_output(["git", "ls-tree", "-r", "--name-only", BASE], cwd=ROOT, text=True).splitlines())

def blob(path):
    path = posixpath.normpath(str(path).replace("\\", "/"))
    if path not in TRACKED:
        return None
    p = subprocess.run(["git", "show", f"{BASE}:{path}"], cwd=ROOT, capture_output=True)
    return p.stdout if p.returncode == 0 else None

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def choose(paths):
    for path in paths:
        if path in TRACKED:
            return path
    return paths[0] if paths else None

def declared_files(node):
    if isinstance(node, dict):
        name = next((node[k] for k in ("path", "file", "relative_path", "artifact") if isinstance(node.get(k), str)), None)
        value = next((node[k] for k in ("sha256", "file_sha256", "hash") if isinstance(node.get(k), str) and re.fullmatch(r"[0-9a-f]{64}", node[k])), None)
        if name and value:
            yield name, value
        for key, value in node.items():
            if key.endswith("_sha256") and isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value):
                stem = key[:-7]
                reference = node.get(stem) or node.get("cases" if stem == "case" else stem)
                if isinstance(reference, str) and any(x in reference for x in ("/", ".")):
                    yield reference, value
            if isinstance(value, dict) and ("sha256" in key or key in ("files", "artifacts", "hashes", "sources")):
                for name, sha in value.items():
                    if isinstance(sha, str) and re.fullmatch(r"[0-9a-f]{64}", sha):
                        yield name, sha
                    elif isinstance(sha, dict) and re.fullmatch(r"[0-9a-f]{64}", str(sha.get("sha256", ""))):
                        yield name, sha["sha256"]
            if isinstance(value, (list, dict)):
                yield from declared_files(value)
    elif isinstance(node, list):
        for item in node:
            yield from declared_files(item)

def main():
    special6 = {
        4:"live-audio/backend/validation/real_pipeline_20260729_localwhisper_ark_fish/evidence.json",
        5:"streaming-speech/validation/runs/exp6-4-qwen2audio-whisper-provenance-20260730-v3/manifest.json",
        6:"end-to-end-speech/validation/runs/exp6-5-minicpmo45-20260801-v1/evidence.json",
        7:"controllable-tts/validation/acceptance.json",
        8:"claude-computer-use-native/validation/runs/exp6-7-anthropic-native-20260803-v2/acceptance.json",
        9:"computer-use-open-model/validation/latest.json",
        11:"xlerobot-teleoperation/validation/runs/local-gpu/evidence.json",
        13:"gemini-xlerobot-navigation/validation/runs/local-gpu/evidence.json",
        14:"rgb-sim2real-grasping/validation/runs/local-gpu/evidence.json",
    }
    reports = []
    overrides = {
        "7-2": "chapter7/experiment-7-2-human-benchmark/results.json",
        "7-6": "chapter7/android-world/failure-attribution/manifest.json",
        "7-10": "chapter7/agent-cost-analysis/sample_trace.json",
        "8-6": "chapter8/speech-sft-experiment/validation/exp8-6-20260804-v1/REPORT.md",
        "8-8": "chapter8/prompt-distillation/validation/exp8-8-kimi3-smollm2-20260730/manifest.json",
        "8-17": "chapter8/premature-completion-dpo/validation/train_20260807T163349Z/training_receipt.json",
        "9-3": "chapter9/prompt-auto-optimization/validation/latest.json",
        "9-5": "chapter9/browser-use-rpa/validation/latest.json",
        "9-7": "chapter9/harness-safety-gate/validation/latest.json",
        "10-1": "chapter10/multi-role-transfer/validation/comparison/runs/exp10-1-qwen35flash-20260809-v2/manifest.json",
    }
    for chapter in range(4, 11):
        book = blob(f"book/chapter{chapter}.md").decode("utf-8")
        experiments = re.findall(r'^> \*\*实验 (\d+-\d+)[^：\n]*：([^\n]*?)\*\*', book, re.M)
        ledger_path = f"chapter{chapter}/EXPERIMENT_LEDGER.md"
        ledger = (blob(ledger_path) or blob(f"chapter{chapter}/README.md")).decode("utf-8")
        rows = []
        for exp, title in experiments:
            number = int(exp.split("-")[1])
            line = next((s for s in ledger.splitlines() if re.match(rf"\| {exp} \|", s)), "")
            evidence = None
            expected = None
            if chapter in (4, 5) or chapter == 6 and number <= 3:
                values = re.findall(r'`([^`]+)`', line)
                if values and not (chapter == 5 and number == 15):
                    rel = values[0]
                    if not Path(rel).suffix:
                        rel += "/manifest.json"
                    evidence = f"chapter{chapter}/{rel}"
                    expected = next((x for x in values if re.fullmatch(r"[0-9a-f]{64}", x)), None)
            elif chapter == 6:
                evidence = f"chapter6/{special6[number]}" if number in special6 else None
            else:
                links = re.findall(r'\]\(([^)]+)\)', line)
                paths = re.findall(r'`([^`]+\.(?:json|md))`', line)
                candidates = []
                for p in links + paths:
                    if p.startswith("http"):
                        continue
                    path = posixpath.normpath(f"chapter{chapter}/{p}")
                    if any(x in p for x in ("validation/", "results/", "TRAINING_REPORT")):
                        if path.endswith("/"):
                            path += "manifest.json"
                        if Path(path).suffix not in (".json", ".md"):
                            path += "/manifest.json"
                        candidates.append(path)
                evidence = choose(candidates)
                if chapter == 8 and number == 1:
                    evidence = "chapter1/learning-from-experience/validation/20260730_011704/evidence.json"
                if chapter == 8 and number == 9:
                    evidence = choose(sorted(p for p in TRACKED if "cot-distillation/" in p and p.endswith("experiment_8_9_complete_20260803_v2.json")))
                if chapter == 9 and number == 8:
                    evidence = "chapter9/hermes-self-evolution/validation/exp9-8-hermes-gpt56luna-autonomous-20260802-v2/manifest.json"
            evidence = overrides.get(exp, evidence)
            raw = blob(evidence) if evidence else None
            row = {"experiment": exp, "title": title, "ledger_row": line, "evidence": evidence,
                   "evidence_in_git": raw is not None, "baseline_sha256": digest(raw) if raw else None,
                   "ledger_hash_matches": digest(raw) == expected if raw is not None and expected else None,
                   "source_kind": "author_saved_history", "new_formal_run": False}
            if raw and evidence.endswith(".json"):
                try:
                    data = json.loads(raw)
                    row["saved_status"] = {k: data[k] for k in ("status", "overall_status", "official_complete", "accepted", "complete") if k in data}
                    declared = sorted(set(declared_files(data)))
                    # Equally spaced deterministic sample, with full count disclosed.
                    sample = declared if len(declared) <= 40 else [declared[i * (len(declared)-1)//39] for i in range(40)]
                    row["declared_hash_entries"] = len(declared)
                    checks = []
                    parent = posixpath.dirname(evidence)
                    project = "/".join(evidence.split("/")[:2])
                    for name, sha in sample:
                        candidates = [posixpath.normpath(f"{parent}/{name}"), posixpath.normpath(f"{project}/{name}"), posixpath.normpath(name)]
                        if "ai-agent-book/" in name:
                            candidates.insert(0, name.split("ai-agent-book/",1)[1])
                        path = next((p for p in candidates if p in TRACKED), candidates[0])
                        item = blob(path)
                        checks.append({"declared_path": name, "resolved_path": path, "in_git": item is not None,
                                       "sha256_matches": digest(item) == sha if item is not None else False})
                    row["sample_checks"] = checks
                except (ValueError, TypeError) as error:
                    row["parse_error"] = str(error)
            rows.append(row)
        out = ROOT / "personal-learning" / f"task{chapter}" / "results" / "saved-evidence-review.json"
        out.parent.mkdir(parents=True, exist_ok=True)
        report = {"baseline_ref": BASE, "scope": "Historical Git blobs only; at most 40 declared artifacts per evidence file, no live API reproduction.",
                  "experiments": len(rows), "evidence_files_present": sum(r["evidence_in_git"] for r in rows), "rows": rows}
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        reports.extend(rows)
        print(f"Chapter {chapter}: {len(rows)} experiments, {report['evidence_files_present']} selected evidence files present", flush=True)
    out = ROOT / "personal-learning" / "chapter4-10-inventory.json"
    out.write_text(json.dumps(reports, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

if __name__ == "__main__":
    main()
