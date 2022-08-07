from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/gigabyte-geforce-rtx-3080-gv-n3080gaming-oc-12gd/p/N82E16814932489"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent # Estrutura de HTML
strong = parent.find("strong")
print(strong.string)