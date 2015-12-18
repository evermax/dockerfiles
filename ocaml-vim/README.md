Build from source:
```
docker build -t dirichlet/ocaml .
```

Run the container and enter the cmd line
```
docker run -i -t dirichlet/ocaml /bin/bash
```
Here there are two disavantages:

 - The work that you do is not persisted
 - If you install new packages they will be lost when you quit and restart the container

Two solutions:
 - `docker run -v /some/local/dir:/some/container/dir -i -y dirichlet/ocaml /bin/bash`
 - link a volume container to /root/.opam
