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
The result might be something like:
```json
{
  "spec": {
    "deployment_resource": {},
    "deployment_source": {
      "docker": {
        "image": "us-central1-docker.pkg.dev/nth-guide-378813/modelzai/mosec-stable-diffusion:23.04.1"
      }
    },
    "framework": "mosec",
    "http_probe_path": "/",
    "id": "0a93636b-5ed3-4abd-8fac-8a7c5a4026c9",
    "image_config": {
      "enable_cache_optimize": false
    },
    "max_replicas": 1,
    "min_replicas": 0,
    "name": "stable-diffusion-mosec",
    "server_resource": "nvidia-tesla-t4-4c-16g",
    "startup_duration": 300,
    "target_load": 10,
    "zero_duration": 300
  },
  "status": {
    "available_replicas": 0,
    "innocation_count": 0,
    "replicas": 0
  }
}
```

#### Step 2: Get Inference Endpoint
After a some time, you could get endpoint of deployment from `list` command.
```shell
modelz deployment list -k mzi-1234567890987654321 -u 00000000-1111-1111-1111-000000000000
```
or `get` command where deployment id of `-d` from `create` command:
```shell
modelz deployment get -k mzi-1234567890987654321 -u 00000000-1111-1111-1111-000000000000 -d 0a93636b-5ed3-4abd-8fac-8a7c5a4026c9
```
The result(get) might be something like:
```json
{
  "spec": {
    "deployment_resource": {},
    "deployment_source": {
      "docker": {
        "image": "us-central1-docker.pkg.dev/nth-guide-378813/modelzai/mosec-stable-diffusion:23.04.1"
      }
    },
    "framework": "mosec",
    "id": "0a93636b-5ed3-4abd-8fac-8a7c5a4026c9",
    "image_config": {
      "enable_cache_optimize": false
    },
    "max_replicas": 1,
    "min_replicas": 0,
    "name": "stable-diffusion-mosec",
    "server_resource": "nvidia-tesla-t4-4c-16g",
    "startup_duration": 300,
    "target_load": 10,
    "zero_duration": 300
  },
  "status": {
    "available_replicas": 0,
    "created_at": "2023-10-12T06:17:15Z",
    "endpoint": "http://stable-diffusion-mosec-vc166fuhjuzkupai.modelz.tech",
    "innocation_count": 0,
    "phase": "NoReplicas",
    "replicas": 0
  }
}
```

#### Step 3: Make Inference
Then you could send any inference you like to the deployment.
```shell
export MODELZ_API_KEY=mzi-1234567890987654321
modelz inference \
--endpoint http://stable-diffusion-mosec-vc166fuhjuzkupai.modelz.tech \
--serde msgpack --write-file cat.jpg cute cat
```

#### Step 4: Delete deployment
When you don't need an deployment any more, don't forget to delete it when you want.
The selected deployment would be deleted immediately.
**This operation can not be undone!**

```shell
export MODELZ_API_KEY=mzi-1234567890987654321
export MODELZ_USER=00000000-1111-1111-1111-000000000000
modelz deployment delete -d b807e092-f748-4d71-8a1d-e57be617c532
```

### Create and infer to ModelZ deployment by code

```python
import time
from modelz import DeploymentClient, ModelzClient
from modelz.openapi.sdk.models import (
    DeploymentSpec,
    DeploymentCreateRequest,
    DeploymentDockerSource,
    DeploymentSource,
    DeploymentSpec,
    DeploymentUpdateRequest,
    FrameworkType,
    ServerResource,
    DeploymentUpdateRequestEnvVars,
)s
from modelz.console import jsonFormattedPrint

# Get ModelZ User ID and API Key from https://cloud.modelz.ai/settings after register.
modelz_user_id = "00000000-1111-1111-1111-000000000000"
modelz_api_key = "mzi-1234567890987654321"

# Create client to operate deployments
client = DeploymentClient(login_name=modelz_user_id, key=modelz_api_key, host="https://cloud.modelz.dev/api/v1")

# Step 1: Create deployment
spec = DeploymentSpec(
        deployment_source=DeploymentSource(
            docker=DeploymentDockerSource(
                image="us-central1-docker.pkg.dev/nth-guide-378813/modelzai/mosec-stable-diffusion:23.04.1")),
        server_resource=ServerResource.NVIDIA_TESLA_T4_4C_16G,
        framework=FrameworkType.MOSEC,
        name="stable-diffusion",
        min_replicas=0,
        max_replicas=1,
        startup_duration=300,
        zero_duration=300,
        target_load=10,
    )
resp = client.create(DeploymentCreateRequest(spec))
print(jsonFormattedPrint(resp))
# Get id of deployment
deployment_id = resp.parsed.spec.id

# Step 2: Get deployments its endpoint for inference
resp = client.get(deployment_id)
print(jsonFormattedPrint(resp))
endpoint = resp.parsed.status.endpoint

# Waiting for ingress created
time.sleep(10)

# Step 3: Make Inference
infer_client = ModelzClient(key=modelz_api_key, endpoint=endpoint, timeout=300)
resp = infer_client.inference(params="cute cat", serde="msgpack")
resp.save_to_file("image.jpg")

# Step 3.1: Update deployment
req = DeploymentUpdateRequest(
    env_vars=DeploymentUpdateRequestEnvVars.from_dict({"debug":"true"})
)
resp = client.update(deployment_id, req)
print(jsonFormattedPrint(resp))

# Step 4: Delete deployment
client.delete(deployment_id)
```

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