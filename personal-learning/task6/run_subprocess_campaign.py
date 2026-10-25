"""Run the four actual subprocess scenarios without changing canonical evidence."""
import asyncio
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'chapter6/async-agent'))
import run_real_experiment as campaign

if __name__=='__main__':
    campaign.VALIDATION_ROOT=HERE/'results'/'subprocess-campaigns'
    print(asyncio.run(campaign.run('local-20261025-v2',0.15)))
