# Makefile for Docker

IMAGE_NAME = tg-bot-template
ENV_FILE = .env

build:
	docker build --tag $(IMAGE_NAME) .

run:
	docker run --env-file $(ENV_FILE) -it $(IMAGE_NAME)

clean:
	docker image rm $(IMAGE_NAME)

build-run:
	docker build --tag $(IMAGE_NAME) .
	docker run --env-file $(ENV_FILE) -it $(IMAGE_NAME)

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f
