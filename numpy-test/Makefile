# https://serverless.com/blog/serverless-python-packaging/

virtualenv:
	docker run -it -v `pwd`:/src --rm virtualenv:latest virtualenv $(RUN_ARGS)


### Commands example
# make virtualenv RUN_ARGS='venv --python=python3'                                                                                                                                2 ↵
# docker run -it -v `pwd`:/src --rm virtualenv:latest venv --python=python3
# created virtual environment CPython3.7.6.final.0-64 in 1515ms
#   creator CPython3Posix(dest=/src/venv, clear=False, global=False)
#   seeder FromAppData(download=False, pip=latest, setuptools=latest, wheel=latest, via=copy, app_data_dir=/tmp/tmp4jv1comu/seed-app-data/v1)
#   activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

source_activate:
	docker run -it -v `pwd`:/src --rm virtualenv:latest source venv/bin/activate

# docker run -it -v `pwd`:/src --rm virtualenv:latest /bin/bash
# root@f056cbb7adcb:/src# source
# bash: source: filename argument required
# source: usage: source filename [arguments]
# root@f056cbb7adcb:/src# source venv/bin/activate
# (venv) root@f056cbb7adcb:/src# 

npm_serveless_python_requirements:
	npm install --save serverless-python-requirements
# Docker Image: lambci/lambda:build-python3.7
