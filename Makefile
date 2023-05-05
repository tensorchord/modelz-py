PY_SOURCE=modelz

# .DEFAULT_GOAL:=build

patch-p: patch install publish push
minor-p: minor install publish push
major-p: major install publish push

build:
	@pdm build

lint:
	@black --check --diff ${PY_SOURCE}
	@ruff check .

format:
	@black ${PY_SOURCE}
	@ruff check --fix .

publish:
	@envchain 'pdm' pdm publish

install:
	pdm install

patch:
	bump2version patch

minor:
	bump2version minor

major:
	bump2version major

push:
	git-pp --push

.PHONY: *