# Project 2 Simple Webpage Deployment using Docker and Google Cloud Platform

- DockerHub: https://hub.docker.com/r/bocaraton/doggif
- GitHub: https://github.com/Tian372/Simple_Webpage_Docker/
- Video Demo: https://youtu.be/GOST0pZBd9o

## DockerHub:

![mydockhub](https://github.com/Tian372/Simple_Webpage_Docker/blob/master/1.png?raw=true)

## Google Cloud Platform

![mygcp](https://github.com/Tian372/Simple_Webpage_Docker/blob/master/2.png?raw=true)

Use `gcloud container clusters create doggif-cluster --num-nodes=3` to create clusters

Use `kubectl create deployment doggif --image=bocaraton/dog-gif` to deploy the application

Use `kubectl expose deployment doggif --type=LoadBalancer --port 80 --target-port 5000` to expose your pods and acess from the internet

## Simple Webpage

![samplepage](https://github.com/Tian372/Simple_Webpage_Docker/blob/master/3.png?raw=true)
