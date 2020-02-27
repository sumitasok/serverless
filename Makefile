setup: venv_build
	npm install -g serverless

create:
	serverless create --template aws-python3 --name numpy-test --path numpy-test

venv_build:
	docker-compose -f "docker-compose.yml" up -d --build 

# make serverless RUN_ARGS='create --template aws-python3 --name mongodb --path mongodb'
serverless:
	docker run -it -v `pwd`:/src --rm serverless:latest serverless $(RUN_ARGS)