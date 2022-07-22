secreto = 'cachorro'
digitadas = []
erradas = []
chances = 5

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'A letra "{letra}" existe na palavra secreta.')
    else:
        print(f'A letra "{letra}" não existe na palavra secreta.')
        erradas.append(letra)
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '_'

    erradas_temporario = ''
    if len(erradas) == 1:
        for erradas_secreto in erradas:
            erradas_temporario += erradas_secreto

    else:
        for erradas_secreto in erradas:
            if len(erradas_temporario) != 0:
                erradas_temporario += ', '
            erradas_temporario += erradas_secreto

    if secreto_temporario == secreto:
        print(f'A palavra era "{secreto_temporario}", você ganhou!')
        break
    else:
        print(f'Erradas: {erradas_temporario}')
        print(f'Palavra: {secreto_temporario}')

    if letra not in secreto:
        chances -= 1

    print(f'Você tem {chances} chances.')
    print()
