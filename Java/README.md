# Java on RunBox

_Java is a general-purpose computer-programming language that is concurrent, class-based, object-oriented, and specifically designed to have as few implementation dependencies as possible._

Running Java code in the cloud on Tenzar RunBox is simple. Assuming you have installed the RunBox CLI, the following commands can be run in your terminal:

1. Download the `HelloWorld.java` file in this folder (or use your own Java code)
2. Import the official [Java image](https://hub.docker.com/_/java/) from Docker Hub

```bash
tenzar import java
```

3. Run a deployment with the image and code

```bash
tenzar run --image java /path/to/HelloWorld.java
```

4. Monitor the deployment status until it is 'running'

```bash
tenzar monitor
```

5. Connect (SSH) to the deployment

```bash
tenzar connect
```

6. Run Java

```bash
$ cd /runbox_volumes
$ javac HelloWorld.java
$ java HelloWorld
Hello, Tenzar RunBox!
```

Finally, you can disconnect with `Ctrl + D` and destroy your deployment with `tenzar destroy [Deployment ID]`
