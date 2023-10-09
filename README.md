# Modelz Python SDK

[Docs](https://tensorchord.github.io/modelz-py/) | [Templates](https://cloud.modelz.ai/templates) | [ModelZ](https://modelz.ai) | [ModelZ Docs](https://docs.modelz.ai/)

[ModelZ](https://modelz.ai) is an MLOps platform, you can deploy serverless instance for machine learning models by packed Docker image, such as Stable Diffusion, Dolly, ImageBind, and so on...

`Deployment` is an instance of any ML service deployed at `ModelZ`, you could create one and then make `inference` to it. 

`Templates` are preset Docker images for `deployment`, which is widely acknowledged used ML models, official templates are built and maintained by `ModelZ` developers. While it's available for you to define your own `template` and `deployment`.

The python SDK is designed for CURD to your `deployments`, and sent request to them to make `inference`. It's an alternative of ModelZ WebUI operation, which could be more friendly with CI/CD pipelines or at model development.

## Install

```shell
pip install modelz-py
```

## CLI usage

We support these functions now:

- create/update/list/delete deployments
- make inference to deployments
- get metric information of any deployment

Those functions will be supported in the future:

- build image and push to registry

**See [CLI Docs](https://tensorchord.github.io/modelz-py/cli.html) for all usages.**

## Example

### Create and infer to ModelZ deployment at terminal

#### Step 1: Create deployment
First, you need to create a deployment at ModelZ platform. We pick `Stable Diffusion` image for this example.
To get more predefined images, see our [templates](https://cloud.modelz.ai/templates).

You can get your ModelZ `API Key` and `User ID` from [here](https://cloud.modelz.ai/settings) after register.

ModelZ supports these type of images:
- DockerHub images: starts with `docker.io/...`, you could build it yourself and upload to DockerHub.
- Google Cloud Registry images: starts with `xxx-docker.pkg.dev/...`, maintainered by ModelZ developers and you could find them at our [Templates](https://cloud.modelz.ai/templates).

```shell
export MODELZ_API_KEY=mzi-1234567890987654321
export MODELZ_USER=00000000-1111-1111-1111-000000000000
modelz deployment create \
--image us-central1-docker.pkg.dev/nth-guide-378813/modelzai/mosec-stable-diffusion:23.04.1 \
--server-resource nvidia-tesla-t4-4c-16g \
--framework mosec \
--name stable-diffusion-mosec
```

#### Step 2: Make Inference
Get endpoint of deployment from `create`command result. If you missed it, you could fetch it from `list` command:
```shell
modelz deployment list -k mzi-1234567890987654321 -n 00000000-1111-1111-1111-000000000000
```

Then you could send any inference you like to the deployment.
```shell
export MODELZ_API_KEY=mzi-1234567890987654321
modelz inference \
--endpoint http://stable-diffusion-mosec-nj6m1uiu0o5bbygs.modelz.tech \
--serde msgpack --write-file cat.jpg cute cat
```

#### Step 3: Delete deployment
When you don't need an deployment any more, don't forget to delete it when you want.
The selected deployment would be deleted immediately.
**This operation can not be undone!**

```shell
export MODELZ_API_KEY=mzi-1234567890987654321
export MODELZ_USER=00000000-1111-1111-1111-000000000000
modelz deployment delete -d b807e092-f748-4d71-8a1d-e57be617c532
```

### Create and infer to ModelZ deployment by code

To be finished...

### Gradio Client on ModelZ Endpoints

We provide a lightweight Python library that makes it very easy to use any Gradio app served on modelz as an API. The functionalities of `GradioClient` are completely identical to `Client` in  `gradio_client` library provided by Gradio. The only difference is that when initializing the client, you should enter your Modelz serving endpoint URL instead of a Hugging Face space.

Example Usage:

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