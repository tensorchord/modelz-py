from unittest.mock import patch

import pytest

from modelz.args import build_argument_parser, parse_arguments


@pytest.mark.parametrize(
    "args, expect_command, expect_args, expect_params",
    [
        (["inference", "-d", "foo"], "inference", {"deployment": "foo"}, None),
        (["metrics", "-d", "foo"], "metrics", {"deployment": "foo"}, None),
        (["build"], "build", {}, None),
        (
            ["inference", "-d", "foo", "--serde", "msgpack"],
            "inference",
            {"deployment": "foo", "serde": "msgpack"},
            None,
        ),
        (
            [
                "inference",
                "-d",
                "foo",
                "--serde",
                "raw",
                "--read-stdin",
                "--write-file",
                "bar",
            ],
            "inference",
            {
                "deployment": "foo",
                "serde": "raw",
                "read_stdin": True,
                "write_file": "bar",
            },
            None,
        ),
        (
            ["inference", "-d", "foo", "draw a cat"],
            "inference",
            {"deployment": "foo"},
            "draw a cat",
        ),
        (
            ["inference", "-d", "foo", "model=llm", "prompt=chat like a cat"],
            "inference",
            {"deployment": "foo"},
            {"model": "llm", "prompt": "chat like a cat"},
        ),
    ],
)
def test_parse_arguments(args, expect_command, expect_args, expect_params):
    with patch("sys.argv", ["modelz"] + args):
        command, arguments, params = parse_arguments(build_argument_parser())
        assert command == expect_command
        assert params == expect_params
        for key, value in expect_args.items():
            assert arguments[key] == value
