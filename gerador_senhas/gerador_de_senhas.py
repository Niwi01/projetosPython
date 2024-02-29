import string
import random


def ger_senha(tamanho,caracteres):
    # caracteres:
    simbolos, numeros, minusculos, maiusculos=string.punctuation, string.digits, string.ascii_lowercase, string.ascii_uppercase

    # string vazia para ser preenchida
    senha=''

    # loop em cada caractere solicitado
    for c in caracteres:
        if '1' in c:
            # vai adicionar as letras Maiúsculos à variavel "senha" 
            senha+=maiusculos
        if '2' in c:
            senha+=minusculos
        if '3' in c:
            senha+=numeros
        if '4' in c:
            senha+=simbolos
        
        # o "join" junta os caracteres aleatórios da variavel "senha" sem espaço.
        # o loop gera a quantidade escolhida da variável "tamanho", resultando uma senha com o tamanho desejado.
    senha_gerada=''.join(random.choice(senha) for _ in range(tamanho))
        
    return senha_gerada

try:
    while True:
        tamanho_senha = int(input('Tamanho da senha:\n'))
        if tamanho_senha <=0:
            print('Tamanho inválido. Por favor, digite um número maior!\n')
            continue

        caracteres=list(map(str,input('Escolha o caractere (ex.: 1,2,3):\n1.Maiúsculos\n2.Minúsculos\n3.Números\n4.Símbolos\n0.Para sair do programa\n').split(',')))
        if '0' in caracteres: 
            break

        senha=ger_senha(tamanho_senha,caracteres)    
        print(f"Sua senha gerada: {senha}")
    
except (ValueError,IndexError) as e:
    print(f"Erro: {e}")
