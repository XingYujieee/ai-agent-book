"""A malformed local-model response must remain visible in campaign receipts."""

import campaign


class TruncatedClient:
    def chat(self, **request):
        assert request["think"] is False
        return {"message": {"content": '{"findings":[{"type":"email"'}, "prompt_eval_count": 1, "eval_count": 2}


def test_malformed_json_is_recorded_instead_of_crashing():
    receipts = []
    findings, _ = campaign.llm_findings(
        TruncatedClient(), "qwen3:0.6b", "contact me@example.com", "test", receipts
    )
    assert findings == []
    assert len(receipts) == 1
    assert receipts[0]["parse_error"].startswith("JSONDecodeError:")
    assert receipts[0]["response"]["message"]["content"].startswith('{"findings"')
