from argparse import ArgumentParser
from modelz import ModelzClient


parser = ArgumentParser("modelz-test")
parser.add_argument("--host", default="", help="API server host")
parser.add_argument("--key", help="API key")
parser.add_argument("--project", help="Project name")
parser.add_argument(
    "--serde", help="serilization method", choices=("json", "msgpack"), default="json"
)


if __name__ == "__main__":
    args = parser.parse_args()
    client = ModelzClient(
        key=args.key,
        project=args.project,
        host=args.host if args.host else None,
        serde=args.srede,
    )
    resp = client.inference(params={"time": 0})
    print(resp.data)
    print(client.metrics())
