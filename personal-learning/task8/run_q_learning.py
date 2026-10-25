"""Repeat the actual CPU Q-learning arm: 10,000 train + 100 greedy episodes."""
import json
from pathlib import Path
import random
import sys
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/"chapter1/learning-from-experience"))
from rl_agent import QLearningAgent

def main():
    random.seed(42); np.random.seed(42)
    start=time.monotonic()
    agent=QLearningAgent()
    training=agent.train(num_episodes=10000,verbose=False,checkpoint_interval=500)
    evaluation=agent.evaluate(num_episodes=100,verbose=False)
    report={"experiment":"8-1","mode":"actual_local_tabular_training","seed":42,"training_episodes":10000,
            "greedy_evaluation_episodes":100,"environment":"deterministic TreasureHuntGame",
            "seconds":round(time.monotonic()-start,3),"training":{k:v for k,v in training.items() if k not in ("episode_rewards","episode_lengths")},
            "evaluation":evaluation,"scope":"Q-learning arm only; no Kimi or other LLM comparison was run."}
    out=Path(__file__).parent/"results";out.mkdir(parents=True,exist_ok=True)
    (out/"q-learning.json").write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    curve=training["learning_curve"]
    fig,ax=plt.subplots(figsize=(7,4))
    ax.plot([r["episode"] for r in curve],[r["victory_rate"] for r in curve],marker="o")
    ax.set(xlabel="Training episodes",ylabel="Victory rate (last 500 episodes)",ylim=(0,1.05),title="Local Q-learning: seed 42")
    ax.grid(alpha=.2);fig.tight_layout();fig.savefig(out/"q-learning-curve.png",dpi=150);plt.close(fig)
    print(json.dumps(report,ensure_ascii=False))

if __name__=="__main__":main()
