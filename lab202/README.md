# Day 2 Lab 2 - Using Image Streams

## Getting Started 

### Lab Objectives

- Practice working with image streams


###  What you will need?

- A GitHub account to fork/create public repositories
- A DockerHub account to push/pull images from the `docker.io`` registry
- OpenShift Local or OpenShift Developer Sandbox
- Command line tools: `git`, `curl`, `oc`, `podman` or `docker`
- A prior git and docker/podman knowledge is expected. 

## Tasks


### Task 01 

1. In this folder there are two subfolder `v1` and `v2`.
Please clone or download this repository to your machine and change the working directory to the `v1` folder.

```
$ cd  ... openshift-workshop-2023/lab202/v1
$ ls
app.py  Dockerfile  requirements.txt
```

2. The folder contains a small sample Python project with a simple web server implemented with the Flask library.
Let's pick an application name and use it to build a new image! (We're using `myapp` here.)

```
$ podman build -t myapp .
$ podman image ls
```

3. Push the custom image to DockerHub

```
$ podman tag localhost/myapp:latest <dockerhub_username>/myapp:latest
$ podman push localhost/<dockerhub_username>/myapp:latest <dockerhub_username>/myapp:latest
```

4. Import the image to your OpenShift cluster. You can create a new project (except if you using the Dev Sandbox Account)

```
$ oc new-project hello-image-streams
$ oc import-image myapp:latest --from=docker.io/<dockerhub_username>/myapp:latest \
  --confirm --scheduled=true
```
Notice the command line arguments! We enabled the automatic update with the scheduled check 

5. Check the created image stream

```
$ oc get imagestream -o yaml
```


## Task 02

1. Create a new application from the image stream

```
$ oc new-app myapp:latest
```

2. Expose the application

```
$ oc expose deployment myapp --port=5000
$ oc expose svc myapp
```
3. Check you can access the application with an http request:

```
$ curl http://myapp-hello-image-streams.apps-crc.testing
Welcome in Flask application!% 
```

## Task 03

1. Now rebuild the image from v2 folder, retag with Podman and push to DockerHub 

```
$ cd ../v2
$ podman build -t myapp .
$ podman tag localhost/myapp:latest <dockerhub_username>/myapp:latest
$ podman push localhost/<dockerhub_username>/myapp:latest <dockerhub_username>/myapp:latest
```

2. OpenShift periodically checks the image stream for new images. The default period is 15 minutes. Let's have quick break and check back later to confirm the changes have been made.

```
$ oc describe is/myapp
```
You should see both sha256 hashes in a couple of minutes:


```
Name:			myapp
Namespace:		hello-image-streams
Created:		18 minutes ago
Labels:			<none>
Annotations:		openshift.io/image.dockerRepositoryCheck=2023-12-03T12:27:03Z
Image Repository:	default-route-openshift-image-registry.apps-crc.testing/hello-image-streams/myapp
Image Lookup:		local=false
Unique Images:		2
Tags:			1

latest
  updates automatically from registry docker.io/tinmancoding/myapp:latest

  * docker.io/tinmancoding/myapp@sha256:081524b099bb4e0f2aa7e18a27055a33aaf84bc48702017f5763eff7c09bb66b
      About a minute ago
    docker.io/tinmancoding/myapp@sha256:41b0f1c024df515fde49117ad4c4a530f30a122296aa9604164e5b64170543bb
      18 minutes ago

```
