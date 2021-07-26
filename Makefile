test:
	pytest
run:
	python3 main.py
docker-build:
	docker build . -t test:1.0.0
docker-run:
	docker run --rm test:1.0.0