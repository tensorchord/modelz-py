from __future__ import annotations

import argparse
from typing import List


def build_argument_parser():
    parser = argparse.ArgumentParser(
        prog="modelz",
        description="modelz CLI",
    )

    subparser = parser.add_subparsers(dest="command")
    inf_parser = subparser.add_parser(
        "inference",
        epilog="You can pass the `key=value` format parameters after the command"
        "like `modelz inference -d foo model=llm prompt='chat like a cat'`",
    )
    metrics_parser = subparser.add_parser("metrics")
    subparser.add_parser("build")

    # inference
    inf_parser.add_argument(
        "--key",
        help="API key for Modelz, will read from env $MODELZ_API_KEY if not provided",
    )
    inf_parser.add_argument("-d", "--deployment", help="deployment key", required=True)
    inf_parser.add_argument(
        "--serde",
        help="serialization/deserialization method",
        choices=("json", "msgpack", "raw"),
        default="json",
    )
    inf_parser.add_argument(
        "--read-stdin", help="read bytes from stdin", action="store_true"
    )
    inf_parser.add_argument(
        "--write-file", help="write received data to file", default=None
    )

    # metrics
    metrics_parser.add_argument(
        "--key",
        help="API key for Modelz, will read from env $MODELZ_API_KEY if not provided",
    )
    metrics_parser.add_argument(
        "-d", "--deployment", help="deployment key", required=True
    )

    return parser


def parse_arguments(parser: argparse.ArgumentParser):
    known, others = parser.parse_known_args()
    params = parse_unknown_args(others)
    command = known.command
    args = vars(known)
    args.pop("command")
    return command, args, params


def parse_unknown_args(args: List[str]):
    """Parse unknown args to key-value pairs or strings."""
    if not args:
        return None
    if "=" in args[0]:
        return dict(pair.split("=", maxsplit=1) for pair in args)
    if len(args) == 1:
        return args[0]
    raise RuntimeError("failed to parse unknown args")
