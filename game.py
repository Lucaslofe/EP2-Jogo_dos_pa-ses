from dados import *
from funcoes import *
import random

jogar_novamente = 's'

while jogar_novamente == 's':

    lista_de_paises = normaliza(DADOS)

    pais_escolhido = sorteia_pais(lista_de_paises)

    n_tentativas = 20

    print('BEM VINDO AO JOGO DE ADIVINHAR O PAÍS\n')
    print('Comandos:\n dica          - entra no mercado de dicas\n desisto       - desiste da rodada\n inventario    - exibe sua posiçãos\n')
    print('Um país foi escolhido, tente adivinhar!')

    distancias = []
    dicas = []

    while n_tentativas > 0:
        if n_tentativas > 10:
            print('\nVocê tem \033[34m{}\033[m tentativa(s)\n'.format(n_tentativas))
        elif n_tentativas > 5 and n_tentativas <= 10:
            print('\nVocê tem \033[33m{}\033[m tentativa(s)\n'.format(n_tentativas))
        else:
            print('\nVocê tem \033[31m{}\033[m tentativa(s)\n'.format(n_tentativas))

        chute = input('Qual é o seu palpite? ').lower()

        if chute in lista_de_paises:
            if chute == pais_escolhido:
                faltam = 20 - n_tentativas
                print(f'*** parabéns! Você acertou após {faltam} tentativas!\n')
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
                if n_tentativas > 4:
                    n_tentativas -= 4
                    printa_lista_paises(distancias)
                    print('Dicas:')
                    lista_de_paises[pais_escolhido]['bandeira']['outras'] = 0
                    cores_bandeira = []
                    for cor, num in lista_de_paises[pais_escolhido]['bandeira'].items():
                        if num != 0:
                            cores_bandeira.append(cor)
                    cores_bandeira = ', '.join(cores_bandeira)
                    dica1 = (f' - Cores da bandeira: {cores_bandeira}')
                    dicas.append(dica1)
                    for i in dicas:
                        print(i)
                else:
                    print('Não há número de tentativas suficientes')
            elif dica == 2:
                if n_tentativas > 3:
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
                else:
                    print('Não há número de tentativas suficientes')
            elif dica == 3:
                if n_tentativas > 6:
                    n_tentativas -= 6
                    printa_lista_paises(distancias)
                    print('Dicas:')
                    area = lista_de_paises[pais_escolhido]['area']
                    area = milhar(area, '.')
                    dica3 = (f' - Área: {area} km2')
                    dicas.append(dica3)
                    for i in dicas:
                        print(i)
                else:
                    print('Não há número de tentativas suficientes')
            elif dica == 4:
                if n_tentativas > 5:
                    n_tentativas -= 5
                    printa_lista_paises(distancias)
                    print('Dicas:')
                    populacao = lista_de_paises[pais_escolhido]['populacao']
                    populacao = milhar(populacao, '.')
                    dica4 = (f' - População: {populacao} habitantes')
                    dicas.append(dica4)
                    for i in dicas:
                        print(i)
                else:
                    print('Não há número de tentativas suficientes')
            elif dica == 5:
                if n_tentativas > 7:
                    n_tentativas -= 7
                    printa_lista_paises(distancias)
                    print('Dicas:')
                    continente = lista_de_paises[pais_escolhido]['continente']
                    dica5 = (f' - Continente: {continente}')
                    dicas.append(dica5)
                    for i in dicas:
                        print(i)
                else:
                    print('Não há número de tentativas suficientes')
        elif chute.lower() == 'desisto':
            desistir = input('Tem certeza que deseja desistir da rodada? [s|n] ').lower()
            if desistir == 's':
                print(f'>>> Que deselegante desistir, o país era {pais_escolhido}')
                break
        elif chute == 'inventario':
            print('Distâncias:')
            printa_lista_paises(distancias)
            print('Dicas:')
            for i in dicas:
                print(i)
        else:
            print('país desconhecido')
            
    if n_tentativas <= 0:
        print(f"Você perdeu o país era {pais_escolhido}")

    jogar_novamente = input('Jogar novamente? [s|n] ')

print('\nAté a proxima!')