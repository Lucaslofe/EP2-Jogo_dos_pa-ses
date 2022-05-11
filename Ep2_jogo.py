#função para randomizar país
import random 
import json

with open("Jogo Ep2\\RealEP2.json", "r") as f:
    data = json.load(f)

def sorteia_pais(paises):
    lista_paises=[]
    for pais in paises.keys():
        lista_paises.append(pais)
    return random.choice(lista_paises)

print (sorteia_pais(data["DATA"]))
 