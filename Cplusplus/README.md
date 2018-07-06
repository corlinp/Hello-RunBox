# C++ on RunBox

_C++ is a general purpose programming language suited for high speed numerical computations and other scientific computing tasks._

Running C++ code in the cloud on Tenzar RunBox is simple. This example will compile and run a basic program using g++. Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_cpp.cpp` file in this folder
2. Import the official [GCC image](https://hub.docker.com/_/gcc/) from Docker Hub

```bash
tenzar import gcc
```

3. Run a deployment with the image and code

```bash
tenzar run --image gcc /path/to/hello_cpp.cpp
```

4. Monitor the deployment status until it is 'running'

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
$ g++ hello_cpp.cpp -o hello
$ ./hello
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
