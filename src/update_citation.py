import json
import requests
from bs4 import BeautifulSoup
import datetime

def get_citation(name):
	# TODO: add exception
	# name = "BNS-GCN: Efficient Full-Graph Training of Graph Convolutional Networks with Partition-Parallelism and Random Boundary Node Sampling"
	prefix = "https://scholar.google.com/scholar?q=allintitle:"
	scholar_link = prefix + name

	page = requests.get(scholar_link).text
	soup = BeautifulSoup(page, "html.parser")

	cite = soup.find_all("a", href=lambda value: value and value.startswith("/scholar?cites="))
	s = cite[0].text if len(cite) >= 1 else "0"
	s = int(''.join(c for c in s if c.isdigit()))

	return s

with open('../.github/citation/citation.json', 'r') as f:
	table = json.load(f)

sorted_table = sorted(table.items(), key=lambda item: item[1]['last update'])

today = datetime.date.today()

for item in sorted_table[0:3]:
	name = item[0]
	cite = get_citation(name)
	item[1]['citation'] = cite
	item[1]['last update'] = today.strftime("%Y-%m-%d")

table = dict(sorted_table)

with open('../.github/citation/citation.json', 'w') as f:
	json.dump(table, f)
