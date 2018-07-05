# Python on RunBox

*Python is an interpreted high-level programming language for general-purpose programming.*

Running Python code in the cloud on Tenzar RunBox is simple. Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_world.py` file in this folder
2. Import the official [Python image](https://hub.docker.com/_/python/) from Docker Hub. If you're using a framework like PyTorch, you may want to search Docker Hub for a pre-built image.
```bash
tenzar import python
```
3. Run a deployment with the image and code
```bash
tenzar run --image python /path/to/hello_world.py
```
4. Monitor the deployment status with until it is 'running'
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
$ python hello_world.py
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
