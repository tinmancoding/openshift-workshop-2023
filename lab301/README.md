# Day 3 Lab 1 - OpenShift networking

## Getting Started 

### Lab Objectives

-  Learn basic networking.


## Tasks


### Task 01 

1. Deploy an example nginx application using the following command:

```
$ oc new-app --template=openshift/nginx-example --name=my-nginx-example --param=NAME=my-nginx-example
```

2. Check the new resources created from this command.

```
$ oc status
$ oc get all
```
### Task 02

1. Scale up the deploymentconfig to 3 pods.

```
$ oc scale deploymentconfig.apps.openshift.io/my-nginx-example --replicas=3
```

2. Answer the following questions:

- What are the IP addresses of the nginx pods? Is there an easy way to get all the IP addresses with one command?

- What is the IP address of the nginx service?


### Task 03

1. Remove the route and create a new one with edge TLS termination. 

You can use the example cert and key from the examples301 folder.
