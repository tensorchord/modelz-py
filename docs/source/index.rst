.. modelz-py documentation master file, created by
   sphinx-quickstart on Tue Jun  6 12:14:05 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to modelz's documentation!
=====================================

.. toctree::
   :maxdepth: 2
   :caption: Reference:
   :hidden:

   api
   cli


``modelz`` is a Python package for calling model prediction and management APIs that are on the modelz_ platform. We provide both Python SDK and CLI interface.

.. _modelz: https://modelz.ai/

Installation
============

.. tab-set::
   
   .. tab-item:: Install from PyPI

      .. code-block:: bash

         pip install modelz-py

   .. tab-item:: Install from source

      .. code-block:: bash

         pip install git+https://github.com/tensorchord/modelz-py

Examples
========

Check modelz_docs_ for more details.

.. _modelz_docs: https://docs.modelz.ai/frameworks/mosec/imagebind

.. code-block:: python
   :linenos:
   :caption: stable diffusion example

   import modelz


   APIKey = "mzi-abcdefg..."
   
   cli = modelz.ModelzClient(deployment="abcdgefg...", key=APIKey, serde="msgpack")
   cli.inference(params="A dog is running in the grass.").save_to_file("dog.jpg")


.. code-block:: python
   :linenos:
   :caption: image bind example

   import modelz


   APIKey = "mzi-abcdefg..."
   
   cli = modelz.ModelzClient(deployment="imagebind-XXX", key=APIKey)
   
   input = {"model": "imagebind-text", "input": ["A dog", "doggery", "puppy"]},
   resp = cli.inference(params=data, serde="msgpack")
   embeddings = resp["data"]
   for emb in embeddings:
      print(emb['embedding'])