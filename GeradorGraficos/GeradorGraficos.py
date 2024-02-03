import matplotlib.pyplot as plt
try:
    nome = input("Digite seu nome: ")
    
    # O "replace()" substitui os caracteres de espaço " " por uma vazia ""
    # O isalpha() verifica os caracteres para ver se são letras ou não
    if not nome.replace(" ","").isalpha() or not nome:
        raise ValueError("Nome inválido")
    
    print(f"\nBem-vindo(a), {nome}!\nPor favor, preencha os dados:\n")

    #Dados
    dias = int(input("Dia(s): ")) 
    receita = float(input("Salário mensal: ").replace(',','.')) 
    gastos = [float(input(f"Gastos no dia {i+1}: ").replace(',','.')) for i in range(dias)] 
  
    #Validacao
    if dias <= 0 or receita <= 0:
        raise ValueError("Digite o valor acima de 0")
    
    #Calculo
    restante = [receita - sum(gastos[:i+1]) for i in range(dias)]
    saldo_final = restante[-1] #pega o ultimo valor
    dias = list(range(1,dias+1))
    
    #Gráficos
    plt.plot(dias,gastos,marker='o',label="Custos diários",color="blue")
    plt.bar(dias,restante,label="Saldo disponível",width=0.3,alpha=0.4,color="slateblue")
    
    #Adição de linha
    plt.axhline(y=receita,color='indigo',ls='--',label="Renda total") 
    
    #Texto no gráfico
    for d,g,r in zip(dias,gastos,restante):
        plt.text(d,g,f"R$ {g:.2f}",ha="center",va="bottom")
        plt.text(d,r,f"R$ {r:.2f}",ha="center",va="bottom")

    plt.xticks(dias) #fornece rótulos especificos no eixo x 
    plt.title("Variação dos gastos e saldos")
    plt.xlabel("Dias")
    plt.ylabel("R$")
    plt.legend()
    
    plt.show()
    
except (ValueError,TypeError) as e:
    print(f'Error: {e}')
