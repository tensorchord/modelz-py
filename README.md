# TensorChord Modelz Python SDK and CLI

[modelz-py](https://github.com/tensorchord/modelz-py) with aiohttp

Basically, [aioclient.py](modelz/aioclient.py) implements the async / aiohttp versions of `Modelz*` classes,  
and [client.py](modelz/client.py) wraps around them with `asyncio.run()` calls.

- [TensorChord Modelz Python SDK and CLI](#tensorchord-modelz-python-sdk-and-cli)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [CLI Usage](#cli-usage)
  - [Example Usage](#example-usage)
    - [CLI Inference](#cli-inference)
    - [Python Interface](#python-interface)
  - [Develop](#develop)

## Installation

### pipx

This is the recommended installation method if you only want to use the CLI.

```
$ pipx install aiomodelz
```

### [pip](https://pypi.org/project/aiomodelz/)

```
$ pip install aiomodelz
```


## CLI Usage

```shell
$modelz --help

usage: modelz [-h] {inference,metrics,build} ...

modelz CLI

positional arguments:
  {inference,metrics,build}

options:
  -h, --help            show this help message and exit
```

## Example Usage
### CLI Inference

```shell
echo "cute cat" | modelz inference $PROJECT --serde msgpack --write-file cat.jpg --read-stdin
```
### Python Interface

```python
# use dotenv to load env
from dotenv import load_dotenv
load_dotenv()

# example .env:
# MODELZ_API_KEY=mzi-*****
# MODELZ_HOST=https://{}.cloud.modelz.dev/ # use this if you're using the dev modelz cluster
# MODELZ_SSL_VERIFY=0 # disable ssl verification

from modelz import AioModelzClient, ModelzClient
...

```



## Develop

```
$ git clone https://github.com/tddschn/aiomodelz.git
$ cd aiomodelz
$ pdm install
```
