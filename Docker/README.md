# Docker on RunBox

_Docker is a computer program that performs operating-system-level virtualization also known as containerization._

RunBox runs Docker containers, typically imported from Docker Hub, but you can also upload your own custom images. This example will build and run a custom Docker image on the cloud.
Assuming you have the RunBox CLI and Docker installed, the following commands can be run in your terminal:

1. Download `Dockerfile` in this folder
2. Build the image using Docker

```bash
docker build -t hello-runbox /path/to/Dockerfile
```

3. Export the Docker image as a .tar file

```bash
docker save hello-runbox -o hello-runbox.tar
```

4. Upload the image to RunBox

```bash
tenzar upload --image hello-runbox.tar
```

5. Run a deployment with the image

```bash
tenzar run --image hello-runbox
```

6. Monitor the deployment status with until it is 'running'

```bash
tenzar monitor
```

7. Connect (SSH) to the deployment

```bash
tenzar connect
```

8. Confirm that your custom image is running

```bash
$ echo $message
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
