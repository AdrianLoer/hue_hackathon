#!/usr/bin/env bash

docker rm -f hue_server
docker build -t hue_server .
docker run -d --name hue_server -p 80:8080 hue_server
docker logs -f hue_server