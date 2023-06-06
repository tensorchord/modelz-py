PY_SOURCE=modelz tests

.DEFAULT_GOAL:=build

build:
	@pdm build

lint:
	@black --check --diff ${PY_SOURCE}
	@ruff check .

format:
	@black ${PY_SOURCE}
	@ruff check --fix .

test:
	@pytest tests -vv -s

docs:
	@cd docs && make html && cd ..

docs-dev: docs
	@python -m http.server -d docs/build/html -b 127.0.0.1

.PHONY: build lint format test docs
