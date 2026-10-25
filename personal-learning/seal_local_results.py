"""Seal local receipts after review. Hashes establish file identity, not correctness."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
for chapter in range(4,11):
    folder=ROOT/f'task{chapter}'/'results'
    if chapter==4:
        paths=[folder/'saved-evidence-review.json',*sorted((folder/'checks').glob('*'))]
    else:
        paths=sorted(p for p in folder.rglob('*') if p.is_file() and p.name!='local-manifest.json')
    entries=[{'path':p.relative_to(folder).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
             for p in paths if p.is_file()]
    payload={'review_date':'2026-10-25','meaning':'Receipt identity only; experiment scope and failures are documented separately.', 'files':entries}
    (folder/'local-manifest.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'Chapter {chapter}: {len(entries)} files')
