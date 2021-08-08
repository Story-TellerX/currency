SHELL := /bin/bash

manage_py := python3 ./app/manage.py

runserver:
	$(manage_py) runserver

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

gen_data_rate:
	$(manage_py) generate_data

gen_data_contactus:
	$(manage_py) gen_data_contactus

gen_data_bank:
	$(manage_py) gen_data_bank

lint:
	$ flake8 app/

show_urls:
	$(manage_py) show_urls

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

worker:
	cd app && celery -A settings worker -l info --autoscale=0,20

rabbitmq-start:
	sudo service rabbitmq-server start

broker-stop:
	sudo service rabbitmq-server stop

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest app/tests -s -vvv --cov=app --cov-report html && coverage report --fail-under=50

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"
