from pathlib import Path
import json
from datetime import datetime, timezone

from chatgpt.lab_context import ALLEN_LAB_CONTEXT


def ensure_dirs(repo_root: Path):
    for folder in [
        "results/chatgpt",
        "reports/chatgpt",
        "figures/chatgpt",
        "data/chatgpt",
        "docs/chatgpt",
    ]:
        (repo_root / folder).mkdir(parents=True, exist_ok=True)


def bullets(items):
    return "\n".join(f"- {item}" for item in items) if items else "- (none)"


def build_context(repo_root: Path):
    record = {
        **ALLEN_LAB_CONTEXT,
        "generator_track": "chatgpt",
        "source_file": "src/chatgpt/lab_context.py",
        "created_utc": datetime.now(timezone.utc).isoformat(),
    }

    (repo_root / "results/chatgpt/allen_lab_context.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    md = f"""# Allen Lab Context Profile

**Generator track:** ChatGPT  
**Source file:** `src/chatgpt/lab_context.py`

## Institution

{record["institution"]}

## Focus areas

{bullets(record["likely_focus_areas"])}

## Equipment or platforms

{bullets(record["likely_equipment_or_platforms"])}

## Report priorities

{bullets(record["report_priorities"])}
"""

    (repo_root / "reports/chatgpt/allen_lab_context.md").write_text(md, encoding="utf-8")
    return record


def build_source_metadata(repo_root: Path, context: dict):
    source_record = {
        "title": "Example Allen Lab Source for Report-Tool Development",
        "authors": ["Allen Lab / Allen Institute source placeholder"],
        "source_type": "paper_or_dataset_note",
        "institution": "Allen Institute",
        "abstract_or_summary": (
            "This placeholder source represents an Allen Lab research output used to test "
            "context-aware metadata extraction for lab report generation. It includes terms "
            "such as cell types, brain atlas, single-cell sequencing, open science, dataset "
            "provenance, methods traceability, and visualization-ready summaries."
        ),
        "keywords": [
            "cell types",
            "brain atlas",
            "single-cell sequencing",
            "open science",
            "dataset provenance",
            "methods traceability",
            "visualization-ready summaries",
        ],
        "source_url": "",
        "notes": [
            "Replace this placeholder with a specific paper, dataset page, or methods source."
        ],
    }

    text = " ".join(
        [
            source_record["title"],
            source_record["abstract_or_summary"],
            " ".join(source_record["keywords"]),
        ]
    ).lower()

    def matched(items):
        return [x for x in items if x.lower().replace("-", " ") in text.replace("-", " ")]

    artifact = {
        "generator_track": "chatgpt",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_record": source_record,
        "context_matches": {
            "matched_focus_areas": matched(context.get("likely_focus_areas", [])),
            "matched_equipment_or_platforms": matched(context.get("likely_equipment_or_platforms", [])),
            "matched_report_priorities": matched(context.get("report_priorities", [])),
        },
    }

    (repo_root / "results/chatgpt/source_metadata.json").write_text(
        json.dumps(artifact, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    md = f"""# Source Metadata

## Source

**Title:** {source_record["title"]}  
**Institution:** {source_record["institution"]}  
**Source type:** {source_record["source_type"]}

## Keywords

{bullets(source_record["keywords"])}

## Matched focus areas

{bullets(artifact["context_matches"]["matched_focus_areas"])}

## Matched equipment or platforms

{bullets(artifact["context_matches"]["matched_equipment_or_platforms"])}

## Matched report priorities

{bullets(artifact["context_matches"]["matched_report_priorities"])}
"""

    (repo_root / "reports/chatgpt/source_metadata.md").write_text(md, encoding="utf-8")
    return artifact


def build_report_sections(repo_root: Path, metadata: dict):
    source = metadata["source_record"]
    matches = metadata["context_matches"]

    sections = [
        {
            "section_id": "source_overview",
            "title": "Source Overview",
            "content": source["abstract_or_summary"],
        },
        {
            "section_id": "allen_context_match",
            "title": "Allen Lab Context Match",
            "content": {
                "focus_areas": matches["matched_focus_areas"],
                "equipment_or_platforms": matches["matched_equipment_or_platforms"],
                "report_priorities": matches["matched_report_priorities"],
            },
        },
        {
            "section_id": "next_steps",
            "title": "Next Steps",
            "content": [
                "Replace placeholder source with a specific Allen Lab paper or dataset.",
                "Attach methods, figures, and source URLs.",
                "Generate proposal-style report sections.",
            ],
        },
    ]

    artifact = {
        "generator_track": "chatgpt",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "source_title": source["title"],
        "sections": sections,
    }

    (repo_root / "results/chatgpt/report_sections.json").write_text(
        json.dumps(artifact, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    md_parts = ["# Report Sections\n"]
    for section in sections:
        md_parts.append(f"## {section['title']}\n")
        content = section["content"]
        if isinstance(content, dict):
            for key, value in content.items():
                md_parts.append(f"### {key.replace('_', ' ').title()}\n")
                md_parts.append(bullets(value) + "\n")
        elif isinstance(content, list):
            md_parts.append(bullets(content) + "\n")
        else:
            md_parts.append(str(content) + "\n")

    (repo_root / "reports/chatgpt/report_sections.md").write_text(
        "\n".join(md_parts),
        encoding="utf-8",
    )

    return artifact


def main():
    repo_root = Path(__file__).resolve().parents[2]
    ensure_dirs(repo_root)

    context = build_context(repo_root)
    metadata = build_source_metadata(repo_root, context)
    build_report_sections(repo_root, metadata)

    print("Built ChatGPT artifacts:")
    print(" - results/chatgpt/allen_lab_context.json")
    print(" - results/chatgpt/source_metadata.json")
    print(" - results/chatgpt/report_sections.json")
    print(" - reports/chatgpt/allen_lab_context.md")
    print(" - reports/chatgpt/source_metadata.md")
    print(" - reports/chatgpt/report_sections.md")


if __name__ == "__main__":
    main()
