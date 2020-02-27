setup: venv_build
	npm install -g serverless

create:
	serverless create --template aws-python3 --name numpy-test --path numpy-test

venv_build:
	docker-compose -f "docker-compose.yml" up -d --build 
