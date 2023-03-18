# Modelz Python SDK

```shell
pip install modelz-py
```

## CLI

```shell
modelz --help
```

### Stable Diffusion

```shell
echo "cute cat" | modelz inference $PROJECT --serde msgpack --write-file cat.jpg --read-stdin
```
