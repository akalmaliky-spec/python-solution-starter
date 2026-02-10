.PHONY: help install clean test run lint format

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make test     - Run unit tests"
	@echo "  make run      - Run the solution"
	@echo "  make lint     - Run linting checks"
	@echo "  make format   - Format code with black"
	@echo "  make clean    - Clean up generated files"

install:
	python -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

test:
	python -m pytest tests.py -v

run:
	python main.py

lint:
	python -m flake8 main.py tests.py --max-line-length=88

format:
	python -m black main.py tests.py --line-length=88

clean:
	find . -type d -name __pycache__ -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	rm -rf .pytest_cache
	rm -rf .venv
