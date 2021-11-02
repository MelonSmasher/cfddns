#!/usr/bin/env bash

# docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t melonsmasher/cfddns:latest --push .;