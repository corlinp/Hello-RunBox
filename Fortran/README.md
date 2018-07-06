# FORTRAN on RunBox

_Fortran is a general-purpose, compiled imperative programming language that is especially suited to numeric computation and scientific computing._

Fortran can be run on Tenzar RunBox in a number of ways. For this exampple we will use an Ubuntu deployment and install & run `gfortran` for a simple Fortran 90 program.

Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_fortran.f90` file in this folder
2. Import [Ubuntu](https://hub.docker.com/_/ubuntu/) from Docker Hub if you haven't already

```bash
tenzar import ubuntu
```

3. Run a deployment with the image and code

```bash
tenzar run --image ubuntu /path/to/hello_fortran.f90
```

4. Monitor the deployment status until it is 'running'

```bash
tenzar monitor
```

5. Connect (SSH) to the deployment

```bash
tenzar connect
```

6. Run Fortran

```bash
$ cd /runbox_volumes
$ apt-get update && apt-get -y install gfortran
$ gfortran hello_fortran.f90 -o hello # This will create a binary executable called hello
$ ./hello
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
