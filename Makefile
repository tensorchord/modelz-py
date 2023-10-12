PY_SOURCE=modelz tests
MODELZ_VERSION?=main

.DEFAULT_GOAL:=build

build:
	@pdm build

build-local:
	@pip install -e .

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

# TODO(junyuchen): Move to 
# gh release download $MODELZ_VERSION --repo tensorchord/modelz -p '*swagger*'
# when swagger goreleaser asset is ready

# Only maintainers of ModelZ could run this command!
# These files are generated:
# - modelz/openapi/swagger.json
openapi-sync:
	@git clone --depth=1 git@github.com:tensorchord/modelz.git --branch ${MODELZ_VERSION} tmp
	@cp tmp/apiserver/pkg/docs/swagger.json modelz/openapi/swagger.json
	@rm -rf tmp

# TODO(junyuchen): Move to generated v3.0 OpenAPI doc when swag supports it
# https://github.com/swaggo/swag/issues/386 and remove convert and pre-fix

# These files are generated:
# - modelz/openapi/swagger_v3.json
# - modelz/openapi/swagger_fix.json
# - modelz/openapi/sdk/*
generate:
	@curl -X 'POST' https://converter.swagger.io/api/convert \
	-H 'Content-Type: application/json' \
	-H 'Accept: application/json' \
	-d @modelz/openapi/swagger.json | jq > modelz/openapi/swagger_v3.json
	@python hack/fix_swag.py
	@rm -rf modelz/openapi/sdk
	@cd modelz/openapi && openapi-python-client generate --path swagger_fix.json \
	--meta none --config ../../hack/openapi-python-client.yaml

.PHONY: build lint format test docs openapi-sync generate
