"""Run three non-actuating local CUDA labs with their original validators.

The chapter renumbered them to 6-11/6-13/6-14; the retained source schemas still
use 6-10/6-12/6-13. This runner records the mapping explicitly.
"""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]
OUT=Path(__file__).resolve().parent/'results'/'gpu'
JOBS=[
    ('6-11','6-10','xlerobot-teleoperation','teleop.py',['--episodes','256','--object-counts','1,2,3','--seeds','20260808,20260809,20260810']),
    ('6-13','6-12','gemini-xlerobot-navigation','desktop_planner.py',[]),
    ('6-14','6-13','rgb-sim2real-grasping','pipeline.py',[]),
]

def main():
    import torch
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA unavailable; refusing to label a CPU debug run as GPU evidence')
    OUT.mkdir(parents=True,exist_ok=True)
    rows=[]
    env=os.environ.copy();env.update(PYTHONIOENCODING='utf-8',PYTHONUTF8='1')
    for current,archived,project,script,args in JOBS:
        target=OUT/current
        cwd=ROOT/'chapter6'/project
        command=[sys.executable,script,*args,'--output-dir',str(target)]
        start=time.monotonic()
        try:
            result=subprocess.run(command,cwd=cwd,env=env,capture_output=True,timeout=240)
            raw=result.stdout+result.stderr;code=result.returncode
        except subprocess.TimeoutExpired as error:
            raw=(error.stdout or b'')+(error.stderr or b'');code=None
        (OUT/f'{current}.txt').write_bytes(raw)
        evidence=target/'evidence.json'
        validation=None
        if code==0 and evidence.exists():
            p=subprocess.run([sys.executable,'validate_evidence.py',str(evidence)],cwd=cwd,env=env,capture_output=True,timeout=30)
            (OUT/f'{current}-validation.txt').write_bytes(p.stdout+p.stderr)
            validation=p.returncode
        row={'current_experiment':current,'archived_schema_id':archived,'kind':'real_local_cuda_simulation','hardware_actuation':False,
             'command':['python',*command[1:]],'script_sha256':hashlib.sha256((cwd/script).read_bytes()).hexdigest(),
             'exit_code':code,'validator_exit_code':validation,'seconds':round(time.monotonic()-start,3),
             'evidence':f'{current}/evidence.json' if evidence.exists() else None}
        rows.append(row)
        (OUT/'summary.json').write_text(json.dumps({'device':torch.cuda.get_device_name(0),'torch':torch.__version__,'runs':rows},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'{current}: run={code}, validator={validation}',flush=True)

if __name__=='__main__':main()
