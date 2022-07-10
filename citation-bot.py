import json
import requests
from bs4 import BeautifulSoup

prefix = "https://scholar.google.com/scholar?q=allintitle:"

name = "BNS-GCN: Efficient Full-Graph Training of Graph Convolutional Networks with Partition-Parallelism and Random Boundary Node Sampling"


scholar_link = prefix + name

page = requests.get(scholar_link).text
soup = BeautifulSoup(page, "html.parser")

print(scholar_link)

print(page)

cite = soup.find_all("a", href=lambda value: value and value.startswith("/scholar?cites="))
s = cite[0].text if len(cite) >= 1 else "0"
s = int(''.join(c for c in s if c.isdigit()))

print(s)
