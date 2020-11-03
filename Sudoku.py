import random


def validar_int(numero, valor=1):
    try:
        numero = int(numero)
        return entrada_scop(numero, valor)
    except ValueError:
        return validar_int(input('\033[31mNúmero Invalido!\n'
                                 'Permitido apenas números inteiros.\033[0m\n'
                                 'Informe Novamente: '))


def entrada_scop(numero, valor):
    if numero < valor or numero > 9:
        return validar_int(input('\033[31mNúmero Invalido!\n'
                                 f'Permitido apenas entre {valor} e 9.\033[0m\n'
                                 'Informe Novamente: '))
    else:
        return numero


def sudoku(lista):
    for i in range(9):
        for s in range(9):
            n = random.randrange(9)
            if n not in lista[i]:
                lista[i].append(n)
            else:
                lista[i].append(0)

    printar(lista)


def solucao(lista):
    for ni, vi in enumerate(lista):
        for nm, vm in enumerate(vi):
            if vm == 0:
                for nn in range(1, 10):
                    if nn not in lista[ni]:
                        lista[ni][nm] = nn
                        break

    printar(lista)


def resolver(lista):
    entrada = [validar_int(input('\nInforme a Linha: ')),
               validar_int(input('Informe a Coluna: ')),
               validar_int(input('Informe o Numero: '), 0)]

    def validar2(v0, v1, v2, v3):
        if entrada[v0] == v1:
            if v0 == 0:
                return 0
            else:
                return 0

        elif entrada[v0] == v2:
            if v0 == 0:
                return 3
            else:
                return 1

        elif entrada[v0] == v3:
            if v0 == 0:
                return 6
            else:
                return 2

    def validar1(posicao, valor):
        if entrada[posicao] <= 3:
            if posicao == 0:
                return validar2(0, 1, 2, 3), validar1(1, 0)
            else:
                res = 0 + valor
                return validar2(1, 1, 2, 3), res

        elif entrada[posicao] <= 6:
            if posicao == 0:
                return validar2(0, 4, 5, 6), validar1(1, 3)
            else:
                res = 1 + valor
                return validar2(1, 4, 5, 6), res

        else:
            if posicao == 0:
                return validar2(0, 7, 8, 9), validar1(1, 6)
            else:
                res = 2 + valor
                return validar2(1, 7, 8, 9), res

    bloco = validar1(0, True)
    lugar = bloco[0] + bloco[1][0]
    lista[bloco[1][1]][lugar] = entrada[2]

    printar(lista)


def verificar(lista):
    for p in range(9):
        for i in range(1, 10):
            if lista[p].count(i) > 1:
                for h in range(lista[p].count(i) - 1):
                    lista[p].remove(i)
                while len(lista[p]) < 9:
                    lista[p].append(0)

    solucao(lista)


def printar(lista):
    print('\n  \033[1;30m  =====  Sudoku!  =====\033[0m')
    v = 1
    print(end=' ')
    for f in range(3):
        print(end='  ')
        for ff in range(3):
            print(f' \033[1;34m{ff + v}', end='')
        v += 3
    print('')
    print(' ', ' \033[1;34m-\033[0m' * 12)

    z = 0
    d = 1
    for t in range(3):
        x = 0
        for i in range(3):
            print(f'\033[1;34m{d} | \033[0m', end='')
            d += 1
            for h in range(3):
                for c in range(3):
                    if c < 3:
                        print(lista[h + z][c + x], end=' ')
                    else:
                        print(lista[h + z][c + x])
                print('\033[1;34m| \033[0m', end='')
            print('')
            x += 3
        z += 3
        print(end='')
        print(' ', ' \033[1;34m-\033[0m' * 12)


def main():
    lista = [[], [], [], [], [], [], [], [], []]
    sudoku(lista)

    while True:
        n = input('''\nOpções: 
    1 - Jogar
    2 - Solução Automatica
    3 - Encerrar
    Informe o Número da Opção: ''')

        if n == '1':
            resolver(lista)
            while True:
                n1 = input('''Opções:
    1 - Continuar
    2 - Terminei
    3 - Solução Automatica
    4 - Desistir
    Informe: ''')
                if n1 == '1':
                    resolver(lista)

                elif n1 == '2':
                    certo = False
                    for p in range(9):
                        if 0 in lista[p]:
                            certo = True
                            break

                        for i in lista[p]:
                            if lista[p].count(i) != 1:
                                certo = True
                                break
                        if certo:
                            break
                    if certo:
                        print('Você Perdeu!')
                    else:
                        print('Parabêns, Você Ganhou!')
                    break

                elif n1 == '3':
                    print('\nResposta:')
                    verificar(lista)
                    break

                elif n1 == '4':
                    break

                elif n1 != '1':
                    print('Código Incorreto.\n')
            break

        elif n == '2':
            print('\nResposta:')
            solucao(lista)
            break

        elif n == '3':
            break

        else:
            print('Código Incorreto.')
    print('\nJogo Finalizado!!!')


main()
