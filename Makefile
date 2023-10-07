PY_SOURCE=modelz tests

.DEFAULT_GOAL:=build

build:
	@pdm build

build-local: build
	@pip uninstall -y modelz-py
	@pip install dist/modelz_py*

lint:
	@black --check --diff ${PY_SOURCE}
	@ruff check . --exclude openapi

format:
	@black ${PY_SOURCE}
	@ruff check --fix .

test:
	@pytest tests -vv -s

docs:
	@cd docs && make html && cd ..

docs-dev: docs
	@python -m http.server -d docs/build/html -b 127.0.0.1

# Move to generated v3.0 OpenAPI doc when swag supports it
# https://github.com/swaggo/swag/issues/386
# Now we need to copy `swagger.json` from `modelz/apiserver/pkg/docs`
openapi-fix:
	@curl -X 'POST' https://converter.swagger.io/api/convert \
	-H 'Content-Type: application/json' \
	-H 'Accept: application/json' \
	-d @openapi/swagger.json | jq > openapi/swagger_v3.json
	@python hack/fix_swag.py

generate:
	@rm -rf openapi/sdk
	@cd openapi && openapi-python-client generate --path swagger_fix.json \
	--meta none --config ../hack/openapi-python-client.yaml

.PHONY: build lint format test docs openapi-install generate
