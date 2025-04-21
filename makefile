default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

gainers:
	python3 get_gainer.py $(SRC); rm raw_data.html; rm raw_data.csv

lint:
	pylint get_gainer.py bin/gainers/ || echo "Linting completed with warnings"

test:
	pytest -vv tests
