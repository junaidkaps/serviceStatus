#Introduction

This is a python based application that queries and returns expected statuses for an environment running 
MongoDB or a proprietary license management system. The actual URL for each of the lms endpoints have been 
removed to protect the vendor's confidentiality. 

Upon receiving an expected response from each service (MongoDB, LMS) the applicaiton converts the output into XML. 
XML is being output since the Pingdom monitoring service does not expect JSON. 

The application was developed using the flask library and wrapped with a Tornado WSGI container to be Production ready. 
Below you will find information on how to create the docker image and deploy the container. 

#Dockerfile

A Dockerfile used to build and deploy the image for the Service Status Application.


## Steps to build and push Service Status Application:
1. Run: docker build -t service_status:1.X  . where X indicates the version number and the "." represents the root of the docker directory.
5. Run: docker tag service_status:1.X --dockerHubUser--/service_status:1.X
6. Run: docker push --dockerHubUser--/service_status:1.X

## Steps to deploy the Service Status Application (Staging):
1. Run: docker run -d -p 5000:5000 -e REDIS_IP=172.30.22.236 -e MONGO_IP=172.30.23.186 -e constraint:node==stg-node-06 --name staging_service_status --dockerHubUser--/service_status:1.2

*Redis and Mongo environment variables are not required to run the root endpoint of the app. 

##Test application 
1. Browser or curl: http://localhost:5000/
2. Test the application running in a production environment at https://status.tallac.com

#Authors
Junaid Kapadia

# License
Copyright © 2016  Tallac Networks. All Rights Reserved
