from dados import *
from funcoes import *

lista_de_paises = normaliza(DADOS)

cores_bandeira = []

capital = lista_de_paises['franca']['capital']
letras = []
for l in capital:
        letras.append(l)
for i in range(len(capital)):
    aleat = random.randint(0, len(letras)-1)
    letra_capital = letras[aleat]
    letras.pop(aleat)


    print(letra_capital)
 


