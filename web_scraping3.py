from bs4 import BeautifulSoup

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")


# procurar em lista []  / procurar copmbinações ao mesmo tempo
tags = doc.find_all(["p", "div","li"]) 
#tag = doc.find_all(["option"], text = "", value = "" ) # [opção] e tag para busca por atributos da tags
#tag['value'] = 'new value'

print(tags)