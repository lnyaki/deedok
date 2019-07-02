#! /bin/sh

DOCKER_NAME="jboost_jenkins"

#First check that a container with that name isn't already present
sudo docker stop $DOCKER_NAME
sudo docker rm $DOCKER_NAME

sudo docker run -d -p 8080:8080 -p 50000:50000 --name $DOCKER_NAME -v $PWD/jenkins:/var/jenkins_home jenkins/jenkins:lts 

