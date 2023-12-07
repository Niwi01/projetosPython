# Aqui teremos operações como adição, substração, multiplicação e divisão
print("Calculora!")
def calculo(num1,num2,escolha):
    if escolha == "+":
        return num1+num2
    elif escolha == "-":
        return num1-num2
    elif escolha == "*":
        return num1*num2
    elif escolha == "/":
        return num1/num2
    else:
        return "Operação inválido!" 
try:        
    fnumero = float(input("Digite um número: "))
    operador = input("Operações disponiveis:\n'+'\n'-'\n'*'\n'/'\n") 
    snumero = float(input("Digite um número: ")) 
    resultado = calculo(fnumero,snumero,operador)
    if fnumero.is_integer() and snumero.is_integer():
        resultado = int(resultado)
    print(resultado)
except ValueError as e:
        print(f"Erro de digitação: {e}")
except ZeroDivisionError:
    print("Não é possível dividir por zero")

    


