run:
	python app/manage.py runserver 0.0.0.0:8000

migrate:
	python app/manage.py migrate

makemigrations:
	python app/manage.py makemigrations

shell:
	python app/manage.py shell_plus --print-sql
