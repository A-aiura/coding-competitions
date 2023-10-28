# =======================
# make
# -----------------------
# make build
# make run
# ...
# =======================

# Set docker image name
IMAGE_NAME=vsc-atcorder- #atcorder-env
CONTAINER_NAME=vsc-atcorder #-container

# Only if you cannot know image/container id
IMAGE_ID := $(shell docker images | grep $(IMAGE_NAME) | awk '{print $$3}')
CONTAINER_ID := $(shell docker ps -a | grep $(CONTAINER_NAME) | awk '{print $$1}')

# Set default target(only `make` to run)
default: help

# Set help messages
help:
	@echo "Usage:"
	@echo "  make build       Build the Docker image."
	@echo "  make run         Run the Docker container."
	@echo "  make start       Start the Docker container."
	@echo "  make stop        Stop the Docker container."
	@echo "  make clean       Stop and remove the Docker container."
	@echo "  make rm          Remove the Docker container."
	@echo "  make rmi         Remove the Docker image."
	@echo "  make show        Show the Docker container."
	@echo "  make showi       Show the Docker images."
	@echo "  make rmu         Remove the unknown Docker container."
	@echo "  make rmiu        Remove the unknown Docker image."

# Build docker image
build:
	docker build -t $(IMAGE_NAME):latest -f ./.devcontainer/Dockerfile .

# Run docker container
run:
	docker run -it --name $(CONTAINER_NAME) \
	-p 8888:8888 \
    -v $(PWD)/workspace:/code/workspace \
    -v $(PWD)/utils:/code/utils \
    -v $(PWD)/atcorder-problems:/code/atcorder-problems \
    $(IMAGE_NAME):latest

# Start docker container
start:
	docker start $(CONTAINER_NAME)
	docker exec -it $(CONTAINER_NAME) /bin/bash

# Stop docker container
stop:
	docker stop $(CONTAINER_NAME)

# Remove docker container
rm:
	docker rm $(CONTAINER_NAME)

# Clean(stop & remove) docker container
clean: stop rm

# Delete docker image
rmi:
	docker rmi $(IMAGE_NAME):latest

show:
	docker ps -a

showi:
	docker images

rmu:
	for c_id in $(CONTAINER_ID) ; do \
		docker rm $$c_id ; \
	done

rmiu:
	for i_id in $(IMAGE_ID) ; do \
		docker rmi $$i_id ; \
	done

.PHONY: default help build run start stop rm clean rmi show showi rmu rmiu
