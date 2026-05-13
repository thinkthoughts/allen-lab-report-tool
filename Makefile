.PHONY: build-chatgpt status

build-chatgpt:
	PYTHONPATH=src python3 src/chatgpt/build_artifacts.py

status:
	git status
