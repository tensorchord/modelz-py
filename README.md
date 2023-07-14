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



## Gradio Client on Modelz Endpoints

We provide a lightweight Python library that makes it very easy to use any Gradio app served on modelz as an API. The functionalities of `GradioClient` are completely identical to `Client` in  `gradio_client` library provided by Gradio. The only difference is that when initializing the client, you should enter your Modelz serving endpoint URL instead of a Hugging Face space.

### Example Usage

```python
from modelz import GradioClient as Client

# Parameter here is the endpoint of your Modelz deployment
# The format is like https://${DEPOLOYMENT_KEY}.modelz.io/
cli = Client("https://translator-th85ze61tj4n3klc.modelz.io/")

cli.view_api() 
# >> Client.predict() Usage Info
# ---------------------------
# Named API endpoints: 1

#  - predict(text, api_name="/predict") -> output
#     Parameters:
#      - [Textbox] text: str 
#     Returns:
#      - [Textbox] output: str 

      
cli.predict("hallo", api_name="/predict")
# >> "Bonjour."


```

