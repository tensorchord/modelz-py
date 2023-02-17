PY_SOURCE=modelz

.DEFAULT_GOAL:=build

build:
	pdm build

lint:
	ruff check .

format:
	black ${PY_SOURCE}
