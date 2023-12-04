# Day 3 Lab 2 - Creating templates and using helm charts

## Getting Started 

### Lab Objectives

-  Learn how to use templates on OpenShift.


## Tasks


### Task 01 

There's a template definition in the `../examples302/templates/hellogo-template.yaml file in this repository`.

1. Copy this template file and create a new one called my-hellogo-template.yaml.

2. Edit your template file and change the template's name to "my-hellogo"

3. Add a new parameter `REPLICAS` to the template. The default value is 1. Use this parameter in the `deployment.spec.replicas` field. 

4. Verify your work with the `oc process -f ... -o yaml` command.

5. Once you ready, deploy your template to your project:

```
$ oc create -f my-hellogo-template.yaml
```

### Task 02

1. Use your deployed template to create resources.

```
$ oc new-app my-hellogo -p REPLICAS=3
```

2. Verify the created resources with `oc get all`. You should see 3 pods running for the application.


3. Remove the related resources with `oc delete all -l app=hellogo`


### Task 03

1. Open the OpenShift Web Console as Developer and browse the find Chart catalog under the "Add" page.

2. Install something using the web ui. 

3. Check the deployed resources with cli too!
