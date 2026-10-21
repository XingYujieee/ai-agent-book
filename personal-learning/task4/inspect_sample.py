"""Record what the generated Chapter 4 chart and PDF expose as text."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from PIL import Image
from PyPDF2 import PdfReader

HERE = Path(__file__).resolve().parent
SAMPLE = HERE / "results" / "4-3-sample"
CHART = SAMPLE / "sample_chart.png"
PDF = SAMPLE / "sample_report.pdf"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    with Image.open(CHART) as chart:
        size = list(chart.size)
    reader = PdfReader(PDF)
    extracted = " ".join(page.extract_text() or "" for page in reader.pages)
    report = {
        "source": "chapter4/multimodal-agent/create_sample.py",
        "chart": {"path": str(CHART.relative_to(HERE)), "sha256": sha(CHART), "pixels": size},
        "pdf": {"path": str(PDF.relative_to(HERE)), "sha256": sha(PDF), "pages": len(reader.pages)},
        "ground_truth_from_generator": {"Q1": 120, "Q2": 150, "Q3": 95, "Q4": 180},
        "all_exact_chart_values_absent_from_pdf_text": all(
            value not in extracted for value in ("120M", "150M", "95M", "180M")
        ),
        "scope": "Checks the generated fixture and PDF text layer; does not compare three live model paradigms.",
    }
    out = HERE / "results" / "4-3-sample-analysis.json"
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(report["all_exact_chart_values_absent_from_pdf_text"], report["chart"]["pixels"])


if __name__ == "__main__":
    main()
