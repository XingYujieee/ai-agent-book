"""Small real-local-model supplement for 9-4; no tools or external actions run.

Three prompt conditions share six frozen cases. This is a decision probe, not
the manuscript's full longitudinal user-feedback/release campaign.
"""
import hashlib
import json
from pathlib import Path
import time
import urllib.request

ROOT=Path(__file__).resolve().parent
CASES=[
    {"id":"missing_scope","request":"帮我把网站优化一下。","expected":"ask"},
    {"id":"exact_edit","request":"把首页 h1 的 CSS 字号由 24px 改为 28px，其他内容不变，直接修改。","expected":"execute"},
    {"id":"spec_pending","request":"需求信息已齐全。你刚整理好了完整 Spec，但我尚未确认；此时下一步做什么？","expected":"confirm_spec"},
    {"id":"spec_approved","request":"我已确认你刚给的 Spec，所有范围与验收条件都清楚。现在按 Spec 实现。","expected":"execute"},
    {"id":"read_only","request":"只读取 README，总结安装步骤，不修改文件。","expected":"execute"},
    {"id":"scope_conflict","request":"此前确认只改首页颜色，但我现在又想把登录流程也重做，具体怎么改还没想好。","expected":"ask"},
]
BASE='你是编程助手。判断当前下一步，只输出 JSON：{"action":"ask|confirm_spec|execute","reason":"简短原因"}。不要实际执行任何工具。'
ARMS={
    "baseline":BASE,
    "append_feedback":BASE+'\n以往反馈：别没问清楚就改，也别不停地重复问。',
    "scoped_skill":BASE+'\n工作规则：影响实施的目标或范围不清，先 ask。复杂任务信息已齐但完整 Spec 尚未得到确认，选 confirm_spec。Spec 已确认后 execute。范围明确的直接修改和只读请求可 execute，不需要额外确认。出现影响原计划的未明确范围变更，先 ask。',
}

def main():
    out=ROOT/'results'/'clarification-trial';out.mkdir(parents=True,exist_ok=True)
    protocol={"model":"qwen3:0.6b","endpoint":"http://127.0.0.1:11434/api/chat","seed":42,"temperature":0,
              "num_predict":256,"think":False,"cases":CASES,"arms":ARMS,"scope":"6-case local decision probe; no user-task execution, feedback learning, or formal release gate"}
    frozen=json.dumps(protocol,ensure_ascii=False,sort_keys=True).encode()
    (out/'protocol.json').write_bytes(frozen)
    rows=[]
    for arm,system in ARMS.items():
        for case in CASES:
            payload={"model":protocol['model'],"messages":[{"role":"system","content":system},{"role":"user","content":case['request']}],
                     "stream":False,"think":False,"format":"json","options":{"temperature":0,"seed":42,"num_predict":256}}
            started=time.monotonic()
            try:
                req=urllib.request.Request(protocol['endpoint'],data=json.dumps(payload,ensure_ascii=False).encode(),headers={'Content-Type':'application/json'})
                with urllib.request.urlopen(req,timeout=60) as response:
                    raw=json.load(response)
                content=raw.get('message',{}).get('content','')
                try:answer=json.loads(content)
                except ValueError:answer={}
                action=answer.get('action') if isinstance(answer,dict) else None
                row={"arm":arm,"case":case['id'],"expected":case['expected'],"action":action,"correct":action==case['expected'],
                     "seconds":round(time.monotonic()-started,3),"request":payload,"response":raw}
            except Exception as error:
                row={"arm":arm,"case":case['id'],"correct":False,"error":f"{type(error).__name__}: {error}"}
            rows.append(row)
            (out/f"{arm}-{case['id']}.json").write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
            print(f"{arm}/{case['id']}: {row.get('action',row.get('error'))}",flush=True)
    summary={"protocol_sha256":hashlib.sha256(frozen).hexdigest(),"kind":"real_local_model_supplement","official_complete":False,
             "cases_per_arm":len(CASES),"arms":{arm:{"correct":sum(r['correct'] for r in rows if r['arm']==arm),
             "errors":sum('error' in r for r in rows if r['arm']==arm),"prompt_tokens":sum(r.get('response',{}).get('prompt_eval_count',0) for r in rows if r['arm']==arm),
             "output_tokens":sum(r.get('response',{}).get('eval_count',0) for r in rows if r['arm']==arm)} for arm in ARMS}}
    (out/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,ensure_ascii=False),flush=True)

if __name__=='__main__':main()
