from dados import *
from funcoes import *

lista_de_paises = normaliza(DADOS)

pais_escolhido = sorteia_pais(lista_de_paises)
print(pais_escolhido)

n_tentativas = 20

print('BEM VINDO AO JOGO DE ADIVINHAR O PAÍS\n')
print('Comandos:\n dica          - entra no mercado de dicas\n desisto       - desiste da rodada\n inventario    - exibe sua posiçãos\n')
print('Um país foi escolhido, tente adivinhar!\n')

while n_tentativas > 0:
    print('Você tem {} tentativa(s)\n'.format(n_tentativas))
    chute = input('Qual é o seu palpite? ').lower()

    if chute in lista_de_paises:
        if chute == pais_escolhido:
            print('Você ganhou')
            break
        else:
            dist = haversine(EARTH_RADIUS, lista_de_paises[pais_escolhido]['geo']['latitude'],  lista_de_paises[pais_escolhido]['geo']['longitude'],  lista_de_paises[chute]['geo']['latitude'], lista_de_paises[chute]['geo']['longitude'])
            dist = round(dist)
            dist = str(dist).replace('.', ',')
            if len(dist) > 3:
                dist = dist[:len(dist)-3] + '.' + dist[len(dist)-3:]
            print(f'Distâncias:\n {dist} km -> {chute}\n')
            n_tentativas -= 1
    elif chute == 'dica':
        print('Mercado de Dicas')
        print('-'*40)
        print(' 1. Cor da Bandeira    - custa 4 tentativas\n 2. Letra da Capital   - custa 3 tentativas\n 3. Área               - custa 6 tentativas\n 4. População          - custa 5 tentativas\n 5. Continente         - custa 7 tentativas\n 0. Sem dica')
        print('-'*40)
        dica = -1
        while dica != 0 and dica != 1 and dica != 2 and dica != 3 and dica != 4 and dica != 5:
            dica = int(input('Escolha sua opção [0|1|2|3|4|5] : '))
            if dica != 0 or dica != 1 or dica != 2 or dica != 3 or dica != 4 or dica != 5:
                print('Opção invalida')
        