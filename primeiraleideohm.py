print("Bem-vindo a nova calculadora da Lei de Ohm em Python!")
choose = int(input("Qual grandeza você gostaria de calcular?\n\n(1: Tensão | 2: Resistência | 3: Corrente)\n\n"))

def calc(choose):
    if choose == 1:
        R = int(input("Entre com o valor de resistência (em kΩ): \n\n"))
        I = int(input("\n\nEntre com o valor de corrente (em mA): \n\n"))
        print(f"\n\nO valor da tensão elétrica é igual a {(R*1000)*(I/1000)}V.\n\n")
    elif choose == 2:
        V = int(input("Entre com o valor de tensão (em V): \n\n"))
        I = int(input("\n\nEntre com o valor de corrente (em mA): \n\n"))
        print(f"\n\nO valor da resistência elétrica é igual a {V/(I/1000)}Ω.\n\n")
    elif choose == 3:
        V = int(input("Entre com o valor de tensão (em V): \n\n"))
        R = int(input("\n\nEntre com o valor de corrente (em kΩ): \n\n"))
        print(f"\n\nO valor da corrente elétrica é igual a {V/(R*1000)}A.\n\n")
    else:
        print("ERRO: Entrada inválida!")

calc(choose)

print("Desenvolvido por Guilherme Mariano Jovanelli - Engenharia de Controle e Automação - Turma A - SENAI 1.23")