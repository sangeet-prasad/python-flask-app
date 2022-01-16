## python-flask-app
This is simple demo python app which can deployed on a docker and kubernetes platform such as minikube. 

## Environment Setup 

To run this project in a K8s cluster please follow steps below to install 
- kubectl
- docker
- minikube

### kubectl Setup
```bash
$ curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl
$ chmod +x ./kubectl
$ sudo mv ./kubectl /usr/local/bin/kubectl
```

### Docker setup
```bash
$ sudo apt-get update && \
    sudo apt-get install docker.io -y
```

### Minikube setup
```bash
$ curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && chmod +x minikube && sudo mv minikube /usr/local/bin/
```

### Verify minikube installation
```bash
$ minikube version
```

### Start minikube 

```bash
$ minikube start --vm-driver=none
```

## Deploy python-flask-app to minikube 

Fetch the python-flask-app and deploy to minikube 

### Checkout python-flask-app project
Clone this repository and navigate to project folder

```bash
$ git clone git@github.com:sangeet-prasad/python-flask-app.git && cd python-flask-app
```

### (Optional) If sangeetprasad/python-flask-app cannot be fetched from docker hub

To build the docker image locally
```bash
$ sudo docker build -t sangeetprasad/python-flask-app:v1 .
```

### Deploy to minikube

```bash
$ kubectl apply -f k8s/deploy.yml
```

### Check for succesfull deployment of the app and service
```bash
$ kubectl get po | grep hello-app
$ kubectl get svc | grep hello-app
```
There should be for 4 pods deployed in Running state and one NodePort service running on port 30080.

## Testing
To test the app 

### From cli 
```bash
$ curl http://localhost:30080 | grep hello-app
```
When the above command is executed multiple times we should see the response where "podid" will change as request is being load balanced and sent to different pods thereby changing the response content set with "podid" serving it.
```
<h1>Hello Python from hello-app-5794557ccf-podid!</h1>
```

### From a browser
When accessed using http://\<\<localhost or hostname\>\>:30080 the response returned will change color and content depending on the pod serving the request.
