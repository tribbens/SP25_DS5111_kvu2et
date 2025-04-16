default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

gainers:
	python3 bin/get_gainer.py $(SRC)

lint:
	pylint bin/get_gainer.py
	import sys; pylint bin/gainers.base.py
	pylint bin/gainers/template_process.py
	pylint bin/gainers/factory.py
	pylint bin/gainers/yahoo.py
	pylint bin/gainers/wsj.py
	pylint bin/gainers/sa.py

test: lint
	pytest -vv tests
