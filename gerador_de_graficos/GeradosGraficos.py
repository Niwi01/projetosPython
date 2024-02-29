#Seria o arquivo final, sua metade está quase pronta, pois falta testar seus erros no except
# e implementar o calculo e o(s) gráfico(s)

import matplotlib.pyplot as plt

#PRIMEIRA PARTE
try:
    name = input("Digite seu nome: ")
    
    # O "replace()" substitui os caracteres de espaço " " por uma vazia ""
    # O isalpha() verifica os caracteres para ver se são letras ou não
    if not name.replace(" ","").isalpha():
        raise ValueError
    
    print(f"\nOlá, {name}. Bem-vindo(a)!\n")
    print(f"Agora, {name}, preencha os dados:\n")


    #Dados
    dias = int(input("Dia(s): "))
    receita = float(input("Salário mensal: ").replace(',','.')) 
    gastos = [float(input(f"Gastos no dia {i+1}: ").replace(',','.')) for i in range(dias)] 
  
    #Calculos
    media_gastos = sum(gastos)/dias if dias>0 else 0
    media_porcentagem_receita = (media_gastos/receita)*100 if receita>0 else 0
    dias = list(range(1,dias+1))


    #Resultado inicial
    print(f"Média de gasto: {media_gastos:.2f} de {sum(gastos)}\nE sua média salarial gasta é: {media_porcentagem_receita:.2f}% de {receita}")

    plt.plot(dias,gastos,linewidth=2.0,marker='o')
    plt.xticks(range(min(dias),max(dias)+1))
    #plt.text(2.5,"")
    plt.title("Variação dos gastos ao londo dos dias")
    plt.show()

except ValueError as e:
        print(f'Erro: {e}')