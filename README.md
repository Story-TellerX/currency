# currency rate project

*This is a tutorial project for developing a backend application using the Django framework.*

*Project using Django templates as frontend, Django framework as backend, 
RabbitMQ as broker, Celery as workers and crontab (beat) for periodically tasks*

The application collects data on exchange rates.

For install project on Ubuntu 20.04 use:

`$ git clone [repository address]`

2) Create virtual environment:

`$ python3 -m venv [venv name]`

3) Activate virtual environment:

`$ . [venv name]/bin/activate`

4) Install packages from requirements:

`$ pip install -r requirements.txt`

5) Create db for app (from app dir):

`$ python3 ./app/manage.py migrate`

6) Run server:

`$ python3 ./app/manage.py runserver`

7) For run ipython console with sql print:

`$ python3 ./app/manage.py shell_plus --print-sql`

8) More common commands in the Makefile. For using Makefile commands use construction:

`$ make [command name]`
