run:
	docker container run --rm -p 8888:8888 -v $$(pwd):/home/jovyan/dev jup

build:
	docker image build -t jup .

build-new:
	docker image rm -f jup
	docker image build -t jup .

