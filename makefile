default:
	@cat makefile

env:
	python3 -m venv env; . env/bin/activate; pip install --upgrade pip

update: env
	. env/bin/activate; pip install -r requirements.txt

ygainers.html: clean_ygainers
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200' > ygainers.html

ygainers.csv: ygainers.html
	python3 -c "import pandas as pd; raw = pd.read_html('ygainers.html'); raw[0].to_csv('ygainers.csv')"

wsjgainers.html: clean_wsjgainers
	sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 'https://www.wsj.com/market-data/stocks/us/movers' > wsjgainers.html

wsjgainers.csv: wsjgainers.html
	python3 -c "import pandas as pd; raw = pd.read_html('wsjgainers.html'); raw[0].to_csv('wsjgainers.csv')"

lint:
	pylint bin/normalize_csv.py

test: lint
	pytest -vv tests

clean_ygainers:
	rm ygainers.html || true
	rm ygainers.csv || true

clean_wsjgainers:
	rm wsjgainers.html || true
	rm wsjgainers.csv || true
