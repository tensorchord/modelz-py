# TensorChord Modelz Python SDK and CLI

[modelz-py](https://github.com/tensorchord/modelz-py) with aiohttp

Basically, [aioclient.py](modelz/aioclient.py) implements the async / aiohttp versions of `Modelz*` classes,  
and [client.py](modelz/client.py) wraps around it with `asyncio.run()` calls.

- [TensorChord Modelz Python SDK and CLI](#tensorchord-modelz-python-sdk-and-cli)
  - [Installation](#installation)
    - [pipx](#pipx)
    - [pip](#pip)
  - [CLI Usage](#cli-usage)
  - [Example Usage](#example-usage)
    - [Stable Diffusion](#stable-diffusion)
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
### Stable Diffusion

```shell
echo "cute cat" | modelz inference $PROJECT --serde msgpack --write-file cat.jpg --read-stdin
```

## Develop

```
$ git clone https://github.com/tddschn/aiomodelz.git
$ cd aiomodelz
$ pdm install
```