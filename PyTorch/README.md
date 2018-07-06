# PyTorch on RunBox

_PyTorch is a deep learning framework for fast, flexible experimentation in Python._

RunBox can be used to run PyTorch models and analysis in the cloud. This example will import an image, run a deployment, and run some Python code that uses `torch`. Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_pytorch.py` file in this folder
2. Import the [PyTorch image](https://hub.docker.com/r/pytorch/pytorch/) from Docker Hub.

```bash
tenzar import pytorch/pytorch
```

3. Run a deployment with the image and code

```bash
tenzar run --image pytorch /path/to/hello_pytorch.py
```

4. Monitor the deployment status until it is 'running'

```bash
tenzar monitor
```

5. Connect (SSH) to the deployment

```bash
tenzar connect
```

6. Run Python

```bash
$ cd /runbox_volumes
$ python hello_pytorch.py
tensor([[-6.7238e+10,  4.5782e-41],
       [-6.6745e-12,  3.0815e-41],
       [ 4.4842e-44,  0.0000e+00]])
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
