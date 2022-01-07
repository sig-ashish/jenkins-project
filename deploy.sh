echo " Deploying to cluster "

/usr/local/bin/kubectl create -f deployment.yaml -f service.yaml
