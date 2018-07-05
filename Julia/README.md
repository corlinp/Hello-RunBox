# Julia on RunBox

*Julia is a high-level, high-performance dynamic programming language for numerical computing.*

Running Julia code in the cloud on Tenzar RunBox is simple. Make sure you have installed the RunBox CLI. The following commands can then be run in your terminal.

1. Download the `hello_world.jl` file in this folder
2. Import the official [Julia image](https://hub.docker.com/_/julia/) from Docker Hub
```bash
tenzar import julia
```
3. Run a deployment with the image and code
```bash
tenzar run --image julia /path/to/hello_world.jl
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
$ julia hello_world.jl
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
