#Este aqui é uma variavel de teste rápido para criar gráficos 
#para testar se consigo entender e fzr os gráficos com sentido
#Este foi o arquivo que fiquei fazendo meus ULTIMOS TESTES

import matplotlib.pyplot as plt

dias=7
gasto = [100,150,200,120,180,130,160] #[float(input("gastos: ").replace(",",".")) for i in range(dias)]
salario = 1500 #float(input("Salario: ").replace(",","."))

#CALCULO
media_gastos=sum(gasto)/dias if dias>0 else 0
media_salario = salario/media_gastos
"""print(f"soma dos gastos:{gasto}\nMedia do gasto:{media_gastos:.2f}")
print(f"Media do salario:{media_salario:.2f} em relacao aos gastos {sum(gasto)}")
"""
dias=list(range(1,dias+1))



#GRAFICOS
"""
plt.bar(dias,media_gastos,label="Media de gastos",width=0.3)
#ticks-> especifica onde os marcadores devem aparecer no eixo 
plt.xticks(range(min(dias),max(dias)+1)) 

"""

plt.subplot(121)
plt.bar(dias,gasto,width=0.3,color='pink',label="Despesas por dia")
plt.xticks(range(min(dias),max(dias)+1)) 
plt.title('Despesa')
plt.xlabel('Dias')
plt.ylabel('Gastos em R$')
plt.legend()
#Media de gastos: mostra se o gasto está superior ou inferior a média
#Ou seja, se tiver acima da linha da media, estara gastando mais doq a media diaria

#-------------------------------
plt.subplot(122)
restante = [salario - g for g in gasto]
plt.plot(gasto,restante,marker='o',label="Salario")
plt.axhline(y=salario,linestyle='--',color='purple')
plt.title('Variação do dinheiro restante em relacao aos gastos')


plt.xlabel('Despesa em R$')
plt.ylabel('Restante do salario em R$')
plt.legend()
plt.show()

