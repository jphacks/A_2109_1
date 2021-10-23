.PHONY: all
all: run

.PHONY: build
build:
	docker-compose build

.PHONY: run
run: build
	docker-compose up	
