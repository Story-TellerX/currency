SHELL := /bin/bash

manage_py := python3 ./app/manage.py

runserver:
	$(manage_py) runserver

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
