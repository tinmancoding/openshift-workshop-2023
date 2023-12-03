# Day 2 Lab 3 - Build Configs with Docker Strategy

## Getting Started 

### Lab Objectives

- Practice creating build configuration with the Docker strategy


###  What you will need?

- A GitHub account to fork/create public repositories
- A DockerHub account to push/pull images from the `docker.io`` registry
- OpenShift Local or OpenShift Developer Sandbox
- Command line tools: `git`, `curl`, `oc`, `podman` or `docker`
- A prior git and docker/podman knowledge is expected. 

## Tasks


### Task 01 

We're going to revisit the oc-fastapi repository from lab201. So, fork the following repository if you haven't forked before: 

```
https://github.com/tinmancoding/oc-fastapi
```
There's a branch called `bc-docker` where I changed some things.
- The Dockerfile moved to a `deployment` folder
- I've added some sample resource yaml files, apply these:

```
$ oc new-project bc-docker-fastapi
$ oc apply -f deployment/imagestream_python.yaml
$ oc apply -f deployment/buildconfig.yaml

```
If you try to start the build it will fail. Your objective is to fix the build config.

```
$ oc start-build bc-docker-fastapi
```

Tips: 
- Use the `oc get all` and `oc describe ...` commands to figure out what are the problems.
- Once you solved the first problem, there is still something missing.

```
$ oc explain bc.spec.strategy
```

Congrats, if you managed to build the image like this:

```
...
pod/bc-docker-fastapi-2-build   0/1     Completed    0          3m34s
...
```
