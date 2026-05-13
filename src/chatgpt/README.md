# src/chatgpt

ChatGPT-generated source code for `allen-lab-report-tool`.

This folder is used to compare ChatGPT implementation choices against other AI-generated tracks while keeping the repo structure clean.

## Purpose

Code here should support reproducible lab-report generation from scientific materials.

Initial goals:

- parse source metadata
- structure report sections
- define reusable schemas
- generate markdown outputs
- support notebook experiments in `notebooks/chatgpt/`
- keep implementation minimal and inspectable

## Suggested structure

```text
src/chatgpt/
  __init__.py
  schemas.py
  report_builder.py
  metadata.py
  exporters.py
