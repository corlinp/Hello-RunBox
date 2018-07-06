# Python on RunBox

_Python is an interpreted high-level programming language for general-purpose programming._

Tenzar RunBox can launch deployments with images that have Python and associated frameworks preinstalled. This guide will run a simple 'hello world' program in base Python. If you're using a framework like [PyTorch](/PyTorch), you may want to search Docker Hub for a pre-built image. For simpler libraries, `pip install` will work.

Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_python.py` file in this folder
2. Import the official [Python image](https://hub.docker.com/_/python/) from Docker Hub.

```bash
tenzar import python
```

3. Run a deployment with the image and code

```bash
tenzar run --image python /path/to/hello_python.py
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
$ python hello_python.py
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
