# Day 2 Lab 1 - Deploy Applications from git and DockerHub

## Getting Started 

### Lab Objectives

- Practice the `oc new-app` command
- Install workloads from git repository (using the Docker build strategy)
- Install workloads from docker images


###  What you will need?

- A GitHub account to fork/create public repositories
- A DockerHub account to push/pull images from the `docker.io`` registry
- OpenShift Local or OpenShift Developer Sandbox
- Command line tools: `git`, `curl`, `oc`, `podman` or `docker`
- A prior git and docker/podman knowledge is expected. 

## Tasks


### Task 01 

1. Open the <https://github.com/tinmancoding/oc-fastapi> repository in your browser and create a fork from it.
You're going to work on your own fork from now on. 

2. Let's use the forked repository to deploy the sample application to your OpenShift cluster.

```
$ oc new-project myfastapi  # on the dev sandbox you can ignore this line
$ oc new-app --name=myfastapi https://github.com/<YOUR GITHUB USERNAME>/oc-fastapi.git

```

3. Let's review the resources created in the project

```
$ oc get all -l app=myfastapi
```

4. Expose the deployment by creating a service and a route resources

```
$ oc expose deployment/myfastapi --port 8080
$ oc expose svc/myfastapi
```

5. Verify that you can access the service on the route's host

```
$ curl "http://$(oc get route fastapi --template '{{ .spec.host }}')"
```

6. If everything is OK, you can remove the resources for this app.

```
$ oc delete all -l app=myfastapi
```


## Task 02

1. Clone *your* oc-fastapi repository to your machine with the `git clone` Command

2. Create a new local branch called `feature-lab201-task02`

3. Open the `app/main.py` file and change the "World" word in the HelloWorld example to "Lab201"

4. Create a commit and push the branch to origin

```
$ git add app/main.py
$ git commit -m "lab201 task02 implemented"
$ git push -u origin feature-lab201-task02
```

5. Deploy a new application using this feature branch instead of main.
The steps are the same, you just need to specify the branch for the `oc new-app` command.
Tip: Check the built-in help for the command by running `oc new-app -h`


6. Practice the most common commands to get an understanding what's the current state of your project:

```
$ oc status
$ oc get all
$ oc get deployment/myfastapi -o yaml
$ oc describe deployment/myfastapi 
```


## Task 03

1. You're in your oc-fastapi project standing on the `feature-lab201-task02` branch.
Create a new branch based on this branch by running:

```
$ git checkout -b feature-lab201-task03
```

2. Build an image locally and push it to your DockerHub account as `YOUR_DOCKERHUB_USERNAME/oc-fastapi:lab201-task03`


3. Deploy the application to OpenShift based on the DockerHub images

```
$ oc new-app YOUR_DOCKERHUB_USERNAME/oc-fastapi:lab201-task3 --name=fastapi-task03
```

4. Verify that the deployment and the image stream have been created.


# Finishing the lab and cleanup (optional)

You can safely remove the resources created on your OpenShift cluster in this lab.


