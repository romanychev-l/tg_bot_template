# Makefile for Docker

IMAGE_NAME = univision
ENV_FILE = .env

build:
	docker build --tag $(IMAGE_NAME) .

run:
	docker run --env-file $(ENV_FILE) --network="host" -it $(IMAGE_NAME)

clean:
	docker image rm $(IMAGE_NAME)

runn:
	docker build --tag $(IMAGE_NAME) .
	docker run --env-file $(ENV_FILE) --network="host" -it $(IMAGE_NAME)