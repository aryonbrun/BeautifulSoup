from bs4 import BeautifulSoup
import re #REGULAR EXPRESSIOn

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# procurar em lista []  / procurar copmbinações ao mesmo tempo

# PROCURAR CLASSES

# tags = doc.find_all(class_="btn-item") # forma de procurar classe

tags = doc.find_all(text = re.compile("\$.*")) # DAR MATCH COM O QUE PROCURA 

for tag in tags: 
    print(tag.strip())
