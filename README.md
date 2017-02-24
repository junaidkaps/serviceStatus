#Dockerfile

A Dockerfile used to build and deploy the image for the Service Status Application.


## Steps to build and push Service Status Application:
1. Run docker build -t service_status:1.X  . where X indicates the version number and the "." represents the root of the docker directory.
5. Run docker tag service_status:1.X docker.tallac.com/tallac/service_status:1.X
6. Run docker push docker.tallac.com/tallac/service_status:1.X

## Steps to deploy the Service Status Application (Staging):
1. Run 	docker run -d -p 5000:5000 -e REDIS_IP=172.30.22.236 -e MONGO_IP=172.30.23.186 -e constraint:node==stg-node-06 --name staging_service_status URL/VENDOR/service_status:1.2


#Authors
Junaid Kapadia

# License
Copyright © 2016  Tallac Networks. All Rights Reserved
