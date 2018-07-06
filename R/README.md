# R on RunBox

_R is a free software environment for statistical computing and graphics._

Tenzar RunBox can be used to run R scripts from a terminal. It does not yet support R Studio. Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_r.r` file in this folder (or use your own code)
2. Import the official [R-base image](https://hub.docker.com/_/r-base/) from Docker Hub

```bash
tenzar import r-base r
```

3. Run a deployment with the image and code

```bash
tenzar run --image r /path/to/hello_r.r
```

4. Monitor the deployment status until it is 'running'

```bash
tenzar monitor
```

5. Connect (SSH) to the deployment

```bash
tenzar connect
```

6. Run your R script

```bash
$ cd /runbox_volumes
$ Rscript hello_r.r
[1] "Hello, Tenzar RunBox!"
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
