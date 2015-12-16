# Netbeans in a container

All credits goes to [Fabio Rehm](https://github.com/fgrehm) for his [repo](https://github.com/fgrehm/docker-netbeans) for this image.

For the way to run graphical app within docker you should check the [post](https://blog.jessfraz.com/post/docker-containers-on-the-desktop/) from Jessie Frazelle, along with her [dockerfiles repo](https://github.com/jfrazelle/dockerfiles).

### Notes

The `--volumes-from maven_data` is a trick that works well if you want to store your maven repositories data into a container as well.
This is a good way to have a good Java development environment that can be easily thrown away when you don't need it anymore.
If you don't need it for now just omit it, but everytime you will build after starting the container, you will have to download all the dependencies again.
Check out the maven container and the explanation on the maven data container [here](https://github.com/evermax/maven-docker).

To run this image do the following:
#### If you are on Linux
```
docker run -ti --rm \
    -e DISPLAY=$DISPLAY \
    -v $HOME/dotfiles/.netbeans-docker:/root/.netbeans \
    -v $(pwd):/workspace \
    --volumes-from maven_data \
    --name netbeans \
    dirichlet/netbeans
```

#### If you are on Mac
You will need [xQuartz](http://www.xquartz.org) installed on your computer.
First use socat (got this from the following [issue](https://github.com/docker/docker/issues/8710) on the docker repository)
```
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
```

Then you can do in another terminal:
```
docker run -ti --rm \
    -e DISPLAY=192.168.99.1:0 \
    -v $HOME/dotfiles/.netbeans-docker:/root/.netbeans \
    -v $(pwd):/workspace \
    --volumes-from maven_data \
    --name netbeans \
    dirichlet/netbeans
```

This image will use the current directory as the workspace.

### Tips
If you want the plugins to be persisted into the .netbeans-docker folder, you should do the following:

Tools > Plugins > Settings tab

Then in the `Advanced` section of the Settings tab, select `Force install into user directory` in the `Plugin Install Location` selectbox.



For some reasons on Mac, I didn't managed to make the `Alt+Shift` shortcut works.
So if you are used to use the `Alt+Shift+O` shortcut to `Go to File...` I would advice to change it to something like `Ctrl+Shift+O`. (You'll have then to change the `Open Project...` shortcut but my guess is that it won't be used as often)
