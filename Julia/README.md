# Julia on RunBox

_Julia is a high-level, high-performance dynamic programming language for numerical computing._

Running Julia code in the cloud on Tenzar RunBox is simple. Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_julia.jl` file in this folder
2. Import the official [Julia image](https://hub.docker.com/_/julia/) from Docker Hub

```bash
tenzar import julia
```

3. Run a deployment with the image and code

```bash
tenzar run --image julia /path/to/hello_julia.jl
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
$ julia hello_julia.jl
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
