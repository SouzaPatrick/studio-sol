#!/bin/bash
IMAGE_NAME=flask-python-sample
CONTAINER_NAME=flask-python-sample

## @ Start project
.PHONY: install up down build
install: build up ## Generate the backend image and upload ALL containers in the project

up: ## Starts ALL containers in the project
	@docker-compose up -d
	@sleep 10

down: ## Stop ALL containers in the project
	@docker-compose down

build: ## Create flask image from project
	@docker build -t ${IMAGE_NAME}:latest .
	@sleep 10


## @ Monitor
.PHONY: log
log: ## List the last 100 logs from the flask container
	@docker-compose logs -f --tail 100


## @ Extras
.PHONY: test check_flask_running
test: check_flask_running ## Run tests
	@docker exec -i ${CONTAINER_NAME} sh -c "pytest -v"

check_flask_running:
	@RUNNING=$$(docker ps -f name=${CONTAINER_NAME} --format="{{.ID}}"); \
	echo $${RUNNING}; \
	if [ "$${RUNNING}" = "" ]; then \
		echo "${CONTAINER_NAME} machine must be running to run this command"; \
		exit 1; \
	fi