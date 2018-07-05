# Julia on RunBox

*Julia is a high-level, high-performance dynamic programming language for numerical computing.*

Running Julia code in the cloud on Tenzar RunBox is simple. If you haven't done so already, create a [RunBox account](https://run.tenzar.com/signup) and install the RunBox CLI. The following commands can then be run in your terminal. You can also follow along with the [RunBox Dashboard](https://github.com/corlinp/Hello-RunBox/blob/master/dashboard.md).

1. Download the `hello_world.jl` file in this folder
2. Import the official [Julia image](https://hub.docker.com/_/julia/) from Docker Hub with `tenzar import julia`
3. Run a deployment with the image and code `tenzar run -i julia /path/to/hello_world.jl`
4. Monitor the deployment status with `tenzar monitor` until the deployment is 'running'
5. Connect (SSH) to the deployment `tenzar connect`
6. Once connected, run:

``` bash
$ cd /runbox_volumes
$ julia hello_world.jl

Hello, Tenzar RunBox!
```

Finally, you can disconnect by typing `exit` and destroy your deployment with `tenzar destroy [Deployment ID]`
