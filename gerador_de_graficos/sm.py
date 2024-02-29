#Importações necessárias
import matplotlib.pyplot as plt
#plotar significa criar um gráfico ou gráfico para representar visualmente os dados

dias=int(input(f"Dia(s): "))
receita = float(input("Salário mensal: "))
gastos = [float(input(f"Gasto no dia {i+1}: ").replace(",",".")) for i in range(dias)]

#Calculo
#A soma(despesas) dividida pelo número de elementos(dias) para obter uma visão geral
media_custo = sum(gastos)/dias if dias>0 else 0
#
media_porcentagem_receita = (media_custo/receita)*100 if receita>0 else 0
#sequencia criada para gerar uma lista de contagem de dias para ser capaz de plotar
d_lista = list(range(1,dias+1)) 

print(f"Sua média de gasto é: {media_custo:.2f} de {sum(gastos)}\nE sua média salarial gasta é: {media_porcentagem_receita:.2f}% de {receita}")

#Graficos
plt.plot(d_lista,gastos,label="Gastos diários")
plt.axhline(y=media_custo, linestyle='--', label="Média dos gastos", color="pink")

plt.xlabel("Dias")
plt.ylabel("Gastos")
plt.title("Gráfico do custo e salário")
plt.legend()
plt.show()


#Sugestões:
# tirar os numeros quebrados(dias) do gráfico -> resolvido:plt.xticks(range(min(dias),max(dias)+1)) 
# gráfico redondo (sugestão) 

 