"""
Schemas for ChatGPT-generated lab report tooling.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class LabContext:
    """
    Structured profile for an institution or lab context.
    """

    institution: str
    likely_focus_areas: list[str] = field(default_factory=list)
    likely_equipment_or_platforms: list[str] = field(default_factory=list)
    report_priorities: list[str] = field(default_factory=list)
    assumptions: list[str] = field(default_factory=list)
    review_required: bool = True

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "LabContext":
        return cls(
            institution=data.get("institution", "Unknown institution"),
            likely_focus_areas=data.get("likely_focus_areas", []),
            likely_equipment_or_platforms=data.get("likely_equipment_or_platforms", []),
            report_priorities=data.get("report_priorities", []),
            assumptions=data.get("assumptions", []),
            review_required=data.get("review_required", True),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "institution": self.institution,
            "likely_focus_areas": self.likely_focus_areas,
            "likely_equipment_or_platforms": self.likely_equipment_or_platforms,
            "report_priorities": self.report_priorities,
            "assumptions": self.assumptions,
            "review_required": self.review_required,
        }


@dataclass
class ReportSection:
    """
    Minimal reusable report section.
    """

    title: str
    content: str
    source_notes: list[str] = field(default_factory=list)
    review_required: bool = True

    def to_markdown(self) -> str:
        lines = [f"## {self.title}", "", self.content.strip(), ""]

        if self.source_notes:
            lines.append("### Source / Review Notes")
            for note in self.source_notes:
                lines.append(f"- {note}")
            lines.append("")

        if self.review_required:
            lines.append("_Review required before public use._")
            lines.append("")

        return "\n".join(lines)
