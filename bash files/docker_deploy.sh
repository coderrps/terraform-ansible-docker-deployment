#!/bin/bash

IMAGE="riturps/my-own-images:portfolio-app-v3"
CONTAINER="portfolio-app"

echo "Pulling latest image..."
docker pull $IMAGE

echo "Removing old container..."
docker rm -f $CONTAINER 2>/dev/null || true

echo "Starting new container..."
docker run -d \
  --name $CONTAINER \
  -p 5000:5000 \
  $IMAGE

echo "Deployment completed."
docker ps -a 