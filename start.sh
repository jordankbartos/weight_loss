#!/bin/bash

docker container run --rm -p 8888:8888 -v $(pwd):/home/jovyan/dev jup
