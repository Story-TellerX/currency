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
