"""
ChatGPT Lab Report Tools

Context-aware report-generation helpers for allen-lab-report-tool.
"""

__version__ = "0.1.0"
__author__ = "Dan Hawkley"

from .lab_context import ALLEN_LAB_CONTEXT
from .schemas import LabContext, ReportSection
from .utils import ensure_dir, write_json, write_text

__all__ = [
    "ALLEN_LAB_CONTEXT",
    "LabContext",
    "ReportSection",
    "ensure_dir",
    "write_json",
    "write_text",
]
