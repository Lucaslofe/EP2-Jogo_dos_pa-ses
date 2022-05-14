#nao sei colocar cores da bandeira (dica 1)
from dados import *
from funcoes import *
import random

lista_de_paises = normaliza(DADOS)

pais_escolhido = sorteia_pais(lista_de_paises)
print(pais_escolhido)

n_tentativas = 20

print('BEM VINDO AO JOGO DE ADIVINHAR O PAÍS\n')
print('Comandos:\n dica          - entra no mercado de dicas\n desisto       - desiste da rodada\n inventario    - exibe sua posiçãos\n')
print('Um país foi escolhido, tente adivinhar!')

distancias = []
dicas = []

while n_tentativas > 0:
    print('\nVocê tem {} tentativa(s)\n'.format(n_tentativas))
    chute = input('Qual é o seu palpite? ').lower()

    if chute in lista_de_paises:
        if chute == pais_escolhido:
            print('Você ganhou!!')
            break
        else:
            dist = haversine(EARTH_RADIUS, lista_de_paises[pais_escolhido]['geo']['latitude'],  lista_de_paises[pais_escolhido]['geo']['longitude'],  lista_de_paises[chute]['geo']['latitude'], lista_de_paises[chute]['geo']['longitude'])
            dist = round(dist)
            if len(distancias) == 0:
                distancias.append([chute, dist])
            else:
                distancias = adiciona_em_ordem(chute, dist, distancias)
            print('Distâncias:')
            printa_lista_paises(distancias)
            print('Dicas:')
            for i in dicas:
                print(i)
            n_tentativas -= 1
    elif chute == 'dica'or chute == 'dicas':
        print('Mercado de Dicas')
        print('-'*40)
        print(' 1. Cor da Bandeira    - custa 4 tentativas\n 2. Letra da Capital   - custa 3 tentativas\n 3. Área               - custa 6 tentativas\n 4. População          - custa 5 tentativas\n 5. Continente         - custa 7 tentativas\n 0. Sem dica')
        print('-'*40)
        dica = -1
        dica = int(input('Escolha sua opção [0|1|2|3|4|5] : '))
        while dica != 0 and dica != 1 and dica != 2 and dica != 3 and dica != 4 and dica != 5:
            print('Opção invalida')
            dica = int(input('Escolha sua opção [0|1|2|3|4|5] : '))
        if dica == 1:
            n_tentativas -= 4
            printa_lista_paises(distancias)
            print('Dicas:')
            #cores_bandeira = lista_de_paises[pais_escolhido]['bandeira']
        elif dica == 2:
            n_tentativas -= 3
            printa_lista_paises(distancias)
            print('Dicas:')
            capital = lista_de_paises[pais_escolhido]['capital']
            letras = []
            for l in capital:
                    letras.append(l)
            aleat = random.randint(0, len(letras)-1)
            letra_capital = letras[aleat].lower()
            letras.pop(aleat)
            dica2 = (f' - Letra da capital: {letra_capital}')
            dicas.append(dica2)
            for i in dicas:
                print(i)
        elif dica == 3:
            n_tentativas -= 6
            printa_lista_paises(distancias)
            print('Dicas:')
            area = lista_de_paises[pais_escolhido]['area']
            area = milhar(area, '.')
            dica3 = (f' - Área: {area} km2')
            dicas.append(dica3)
            for i in dicas:
                print(i)
        elif dica == 4:
            n_tentativas -= 5
            printa_lista_paises(distancias)
            print('Dicas:')
            populacao = lista_de_paises[pais_escolhido]['populacao']
            populacao = milhar(populacao, '.')
            dica4 = (f' - População: {populacao} habitantes')
            dicas.append(dica4)
            for i in dicas:
                print(i)
        elif dica == 5:
            n_tentativas -= 7
            printa_lista_paises(distancias)
            print('Dicas:')
            continente = lista_de_paises[pais_escolhido]['continente']
            dica5 = (f' - Continente: {continente}')
            dicas.append(dica5)
            for i in dicas:
                print(i)


            
            
            
    else:
        print('país desconhecido')
        