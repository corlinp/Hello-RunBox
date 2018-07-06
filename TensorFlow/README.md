# TensorFlow on RunBox

_TensorFlow is an open-source software library for dataflow programming across a range of tasks._

Running TensorFlow models on Tenzar RunBox is simple. This example will run a basic TensorFlow session that prints something. The same procedure can be used with your own code. Note that while this uses RunBox's entry node, it is also possible to run on GPU nodes using the `tensorflow/tensorflow:latest-gpu` image and Tenzar's `GC1` or `GC8` nodes.

Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_tensorflow.py` file in this folder
2. Import a [TensorFlow image](https://hub.docker.com/r/tensorflow/tensorflow/) from Docker Hub

```bash
tenzar import tensorflow/tensorflow
```

3. Run a deployment with the image and code

```bash
tenzar run --image tensorflow /path/to/hello_tensorflow.py
```

4. Monitor the deployment status with until it is 'running'

```bash
tenzar monitor
```

5. Connect (SSH) to the deployment

```bash
tenzar connect
```

6. Run Julia

```bash
$ cd /runbox_volumes
$ python hello_tensorflow.py
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
