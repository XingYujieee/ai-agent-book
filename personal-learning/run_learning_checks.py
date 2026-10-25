"""Run bounded, credential-free chapter checks and retain their actual output."""
from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
JOBS = [
    (4, "collaboration", "chapter4/collaboration-tools", ["test_run_experiment_4_5.py"]),
    (5, "handoff", "chapter5/provider-failover", ["tests/test_offline.py"]),
    (5, "math", "chapter5/code-for-math", ["test_campaign.py", "test_empty_problems.py"]),
    (5, "logic", "chapter5/code-for-logic", ["test_hf_dataset.py", "test_parse_answer_boolean.py", "test_silent_resident.py", "test_statistics.py"]),
    (5, "logic-random", "chapter5/code-for-logic", ["test_random_stmt_one_person.py"]),
    (5, "rules", "chapter5/small-model-codified-rules", ["test_campaign.py"]),
    (5, "slides", "chapter5/paper-to-ppt", ["test_null_issues.py", "test_page_contract.py"]),
    (5, "video", "chapter5/paper-to-video", ["test_campaign.py", "test_ffprobe_duration.py", "test_null_bullet_item.py"]),
    (5, "editing", "chapter5/video-edit", ["test_agents_llm_json.py", "test_bare_output_filename.py", "test_extract_json_adjacent.py", "test_slowmo_factor_zero.py", "test_slowmo_null_factor.py"]),
    (5, "cad", "chapter5/cad-vs-diffusion", ["test_offline.py"]),
    (5, "diagnosis", "chapter5/log-diagnosis", ["test_campaign_orchestrator.py", "test_github_mcp_bare_output.py", "test_replay_latency.py"]),
    (5, "form", "chapter5/dynamic-form", ["test_round_trip_destination.py", "test_summarize_numeric_zero_baggage.py"]),
    (5, "erp", "chapter5/erp-agent", ["test_parse_only.py"]),
    (5, "ui", "chapter5/conversational-ui", ["test_customize_malformed_args.py", "test_customize_malformed_json.py", "test_customize_non_dict_file_item.py"]),
    (5, "creator", "chapter5/agent-creator", ["test_creator.py"]),
    (6, "mailbox", "chapter6/agent-with-event-trigger", ["test_unipile_mailbox_experiment.py"]),
    (6, "async", "chapter6/async-agent", ["test_checkpoint_robustness.py", "test_real_experiment.py", "test_real_tasks.py"]),
    (6, "steering", "chapter6/astra-async-steering", ["test_judging.py"]),
    (6, "streaming", "chapter6/streaming-speech", ["test_official_experiment.py", "test_streaming.py", "test_whisper_baseline.py"]),
    (6, "speech", "chapter6/end-to-end-speech", ["tests/test_demo.py", "tests/test_speech_model.py", "tests/test_validate_evidence.py"]),
    (6, "tts", "chapter6/controllable-tts", ["test_fish_s1.py"]),
    (6, "browser", "chapter6/computer-use-open-model", ["tests/test_config.py", "tests/test_evidence.py"]),
    (6, "teleop", "chapter6/xlerobot-teleoperation", ["test_validator.py"]),
    (6, "navigation", "chapter6/gemini-xlerobot-navigation", ["test_validator.py"]),
    (6, "sim2real", "chapter6/rgb-sim2real-grasping", ["test_validator.py"]),
    (7, "rubric", "chapter7/user-memory-system-evaluation", ["test_experiment.py"]),
    (7, "tts-judge", "chapter7/tts-quality-eval", ["tests/test_judge_robustness.py", "tests/test_resolve_gemini_model_null.py"]),
    (7, "elo", "chapter7/elo-leaderboard", ["tests/test_analyze_empty_history.py", "tests/test_animation_empty_history.py", "tests/test_animation_tie_wins.py"]),
    (7, "policy", "chapter7/user-memory-policy-eval", ["test_runner.py"]),
    (7, "cost", "chapter7/agent-cost-analysis", ["tests/test_chat_null_usage.py", "tests/test_trace_offline.py"]),
    (7, "benchmark", "chapter7/model-benchmark", ["test_campaign.py"]),
    (7, "action", "chapter7/model-action-threshold", ["tests/test_experiment.py"]),
    (7, "robot-eval", "chapter7/openvla-robotwin2-eval", ["test_experiment.py"]),
    (7, "android", "chapter7/android-world", ["test_experiment.py"]),
    (8, "prompt-distillation", "chapter8/prompt-distillation", ["test_compare_empty.py", "test_create_data_empty.py", "test_evaluate_empty_parse_rate.py", "test_evaluate_none_pred_label.py", "test_experiment_8_8.py"]),
    (8, "cot", "chapter8/cot-distillation", ["test_analyze_null_assistant_content.py", "test_analyze_short_messages.py", "test_empty_problems.py", "test_load_verified_messages_colon.py", "test_student_pipeline.py"]),
    (8, "dpo", "chapter8/premature-completion-dpo", ["test_pipeline.py"]),
    (8, "quotes", "chapter8/curly-quote-sft", ["tests/test_curly_pipeline.py"]),
    (8, "copy", "chapter8/exact-copy-sft", ["tests/test_copy_pipeline.py"]),
    (8, "speech-sft", "chapter8/speech-sft-experiment", ["test_experiment.py"]),
    (9, "verifier", "chapter9/trajectory-verifier", ["test_verifier.py", "test_claim_action_order.py", "test_empty_dimensions_score.py", "test_llm_judge_null_fields.py"]),
    (9, "prompt", "chapter9/prompt-auto-optimization", ["test_non_dict_edit.py", "test_release_gate_non_dict_edit.py"]),
    (9, "rpa", "chapter9/browser-use-rpa", ["test_state_predicates.py"]),
    (9, "safety", "chapter9/harness-safety-gate", ["test_evolution.py", "test_safety_policy_gate.py"]),
    (9, "evolution", "chapter9/self-evolution-eval", ["test_campaign_statistics.py", "test_longitudinal.py", "test_null_rubric_dimension.py"]),
    (10, "roles", "chapter10/multi-role-transfer", ["tests"]),
    (10, "translation", "chapter10/book-translation", ["tests"]),
    (10, "registration", "chapter10/autonomous-phone-registration", ["test_orchestration.py", "test_validate_acceptance.py"]),
    (10, "parallel", "chapter10/parallel-web-research", ["test_coordination.py", "test_worker_terminate_before_task.py", "test_completed_worker_ack_regression.py"]),
    (10, "social", "chapter10/generative-agents", ["tests/test_campaign_storage.py", "tests/test_judge_plausibility.py", "tests/test_provider_adapter.py", "tests/test_runner_helpers.py"]),
    (10, "werewolf", "chapter10/voice-werewolf", ["test_simultaneous_deaths_consensus.py", "test_witch_killed_no_poison.py"]),
]

def run(job):
    chapter, name, directory, targets = job
    out = ROOT / "personal-learning" / f"task{chapter}" / "results" / "checks"
    out.mkdir(parents=True, exist_ok=True)
    if (out / f"{name}.json").exists():
        attempt = len(list(out.glob(f"{name}.attempt*.json"))) + 1
        for suffix in ("json", "txt"):
            (out / f"{name}.attempt{attempt}.{suffix}").write_bytes((out / f"{name}.{suffix}").read_bytes())
    cmd = [sys.executable, "-m", "pytest", "-q", "-o", "asyncio_mode=auto", *targets]
    env = os.environ.copy()
    env.update(PYTHONIOENCODING="utf-8", PYTHONUTF8="1")
    start = time.monotonic()
    try:
        p = subprocess.run(cmd, cwd=ROOT / directory, env=env, capture_output=True, timeout=150)
        status, code, raw = ("passed" if p.returncode == 0 else "failed"), p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired as error:
        status, code, raw = "timeout", None, (error.stdout or b"") + (error.stderr or b"")
    (out / f"{name}.txt").write_bytes(raw)
    report = {"chapter": chapter, "name": name, "kind": "offline_test", "formal_experiment_completed": False,
              "cwd": directory, "argv": ["python", *cmd[1:]], "status": status, "returncode": code,
              "duration_seconds": round(time.monotonic() - start, 3), "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
              "log": f"{name}.txt"}
    (out / f"{name}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{chapter}/{name}: {status} ({report['duration_seconds']}s)", flush=True)
    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapters", nargs="+", type=int, default=list(range(4, 11)))
    parser.add_argument("--names", nargs="+")
    args = parser.parse_args()
    selected = [j for j in JOBS if j[0] in args.chapters and (not args.names or j[1] in args.names)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(run, selected))
