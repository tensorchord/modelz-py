import logging
from http import HTTPStatus
from unittest.mock import patch

import httpx
import pytest
from click.testing import CliRunner, Result

from modelz.args import inference
from modelz.client import ModelzResponse


@pytest.mark.parametrize(
    "name, args, stdin, expect_serde, expect_params",
    [
        ("basic", ["-e", "foo", "-k", "testkey"], None, "json", None),
        (
            "explicit serde",
            ["-e", "foo", "-k", "testkey", "--serde", "msgpack"],
            None,
            "msgpack",
            None,
        ),
        (
            "stdin param",
            [
                "-e",
                "foo",
                "-k",
                "testkey",
                "--serde",
                "raw",
                "--read-stdin",
            ],
            "data",
            "raw",
            b"data",
        ),
        (
            "unknown param",
            ["-e", "foo", "-k", "testkey", "draw a cat"],
            None,
            "json",
            "draw a cat",
        ),
        (
            "equation param",
            ["-e", "foo", "-k", "testkey", "model=llm", "prompt=chat like a cat"],
            None,
            "json",
            {"model": "llm", "prompt": "chat like a cat"},
        ),
    ],
)
def test_inference_basic(name, args, stdin, expect_serde, expect_params):
    with patch("modelz.client.ModelzClient.inference") as mock_func:
        mock_func.return_value = ModelzResponse(
            resp=httpx.Response(status_code=HTTPStatus.OK)
        )
        runner = CliRunner()
        result = runner.invoke(inference, args, stdin)
        assertResult(result)
        mock_func.assert_called_with(serde=expect_serde, params=expect_params)


@pytest.mark.parametrize(
    "name, args, envs, stdin, expect_serde, expect_params",
    [
        ("basic", ["-e", "foo"], {"MODELZ_API_KEY": "testkey"}, None, "json", None),
    ],
)
def test_inference_env(name, args, envs, stdin, expect_serde, expect_params):
    with patch("modelz.client.ModelzClient.inference") as mock_func:
        mock_func.return_value = ModelzResponse(
            resp=httpx.Response(status_code=HTTPStatus.OK)
        )
        runner = CliRunner(env=envs)
        result = runner.invoke(inference, args, stdin)
        assertResult(result)
        mock_func.assert_called_with(serde=expect_serde, params=expect_params)


def assertResult(result: Result):
    if result.exit_code != 0:
        logging.error("command run failed", exc_info=result.exc_info)
        raise AssertionError("exit code != 0")
