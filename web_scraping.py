from bs4 import BeautifulSoup
import requests

with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

# tag = doc.title
# tag.string = "HELLO"

# print(doc)

tags = doc.find_all("p")[0]

print(tags.find_all)