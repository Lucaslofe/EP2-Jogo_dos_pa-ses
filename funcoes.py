from math import *
import random 

def normaliza(dicionario):
    paises = {}

    for continente in dicionario:
        DATA = dicionario[continente]
        for pais in DATA:
            dados = DATA[pais]
            dados['continente'] = continente
            paises[pais] = dados
    return paises


def sorteia_pais(paises):
    lista_paises = []
    for pais in paises.keys():
        lista_paises.append(pais)
    return random.choice(lista_paises)

def haversine(r, p1, y1, p2, y2):
    p1 = radians(p1)
    y1 = radians(y1)
    p2 = radians(p2)
    y2 = radians(y2)

    c2 = sin((p2-p1)/2)**2
    c3 = cos(p1) * cos(p2) 
    c4 = sin((y2-y1)/2)**2
    c5 = c3*c4
    c6 = c2 + c5
    c7 = sqrt(c6)
    
    c1 = 2 * r * asin(c7)

    return c1

def adiciona_em_ordem(pais, distancia, lista):
    saida = [0] * (len(lista) + 1)
    pos = -1
    for i in range(len(lista)):
        if distancia < lista[i][1]:
            pos = i
            break
    if pos == -1:
        pos = len(lista)  
    for i in range(pos):
        saida[i] = lista[i]
    saida[pos] = [pais, distancia]
    for i in range(pos+1, len(saida)):
        saida[i] = lista[i-1]
    return saida
    

def adiciona_em_ordem(pais, distancia, lista):
    saida = [0] * (len(lista) + 1)
    pos = -1
    for i in range(len(lista)):
        if distancia < lista[i][1]:
            pos = i
            break
    if pos == -1:
        pos = len(lista)  
    for i in range(pos):
        saida[i] = lista[i]
    saida[pos] = [pais, distancia]
    for i in range(pos+1, len(saida)):
        saida[i] = lista[i-1]
    return saida


def milhar(num, sep): 
    s = str(num)
    return s if len(s) <= 3 else milhar(s[:-3], sep) + sep + s[-3:]


def sorteia_letra(palavra, res):
    restricoes = ['.', ',', '-', ';', ' ']
    check = ''
    for i in res:
        restricoes.append(i)
    for i in range(len(palavra)):
        if palavra[i] not in restricoes:
            check = 'ok'
            break
    if check != 'ok':
        return ''
    while True:
        num = random.randint(0, (len(palavra)-1))
        if palavra[num] not in restricoes:
            return palavra[num]
    
def printa_lista_paises(distancias):

    for pais in distancias:
        distancia = pais[1]
        dist = str(distancia).replace('.', ',')
        if len(dist) > 3:
            dist = dist[:len(dist)-3] + '.' + dist[len(dist)-3:]
        nome_pais = pais[0]
        if distancia > 10000:
            print(f' \033[37m{dist} km -> {nome_pais}\033[m')
        elif distancia > 5000:
            print(f' \033[35m{dist} km -> {nome_pais}\033[m')
        elif distancia > 2000:
            print(f' \033[31m{dist} km -> {nome_pais}\033[m')
        elif distancia > 1000:
            print(f' \033[33m{dist} km -> {nome_pais}\033[m')
        else:
            print(f' \033[34m{dist} km -> {nome_pais}\033[m')