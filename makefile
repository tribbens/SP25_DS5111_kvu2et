default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

gainers:
	python3 bin/get_gainer.py $(SRC)

lint:
	pylint bin/normalize_csv.py

test: lint
	pytest -vv tests
