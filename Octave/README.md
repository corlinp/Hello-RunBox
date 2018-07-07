# Octave on RunBox

_GNU Octave is software featuring a high-level programming language, primarily intended for numerical computations._

Tenzar RunBox can be used to run MATLAB scripts with GNU Octave. It does not yet support X11 forwarding for Octave GUIs. Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `hello_octave.m` file in this folder (or use your own code)
2. Import the [Octave image](https://hub.docker.com/r/openmicroscopy/octave/) from Open Microscopy on Docker Hub

```bash
tenzar import openmicroscopy/octave
```

3. Run a deployment with the image and code

```bash
tenzar run --image octave /path/to/hello_octave.m
```

4. Monitor the deployment status until it is 'running'

```bash
tenzar monitor
```

5. Connect (SSH) to the deployment

```bash
tenzar connect
```

6. Run your code

```bash
$ cd /runbox_volumes
$ octave hello_octave.m
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
