extrato = []
saldo = 500


def menu_inicial():
    menu = input("\n1 - Consultar saldo. \n2 - Depositar. \n3 - Sacar. \n4 - Extrato. \n0 - Sair. \n")
    if menu == "1":
        print ("\nSeu saldo atual é de: ", saldo)
        menu_inicial()

    elif menu == "2":
        depositar()

    elif menu == "3":
        sacar()
    
    elif menu == "4":
        exibir_extrato()
    
    elif menu == "0":
        print("Encerrando programa...")
        exit()
    
    else: print ("\nSeleção inválida por favor digite um numero correspondente. ")
    menu_inicial()

def depositar():
    global saldo
    depositar_saldo = input("Digite quanto você deseja depositar ou aperte ENTER para voltar ao menu: ")

    if depositar_saldo == "":
        menu_inicial()

    try:
        depositar_saldo = float(depositar_saldo)

    except ValueError:
        print ("Valor inválido, tente novamente. ")
        depositar()

    if depositar_saldo > 0:
        saldo = saldo + depositar_saldo    
        extrato.append(f"Depósito: +{depositar_saldo}")
        print ("Você depositou $", depositar_saldo, "com sucesso em sua conta, seu saldo atual é de: $", saldo)
        menu_inicial()

    else: print("Valor inválido, tente novamente. ")
    depositar()

def sacar():
    global saldo
    saque = input("Digite quanto você deseja sacar ou aperte ENTER para voltar ao menu: ")
    if saque == "":
        menu_inicial()
    
    try:
        saque = float(saque)

    except ValueError:
        print("\nValor inválido tente novamente.\n")
        sacar()

    if saque <= 0:
        print ("\nValor inválido, tente novamente.\n")
        sacar()

    if saque <= saldo:
        saldo = saldo - saque
        extrato.append(f"Saque: -{saque}")
        print ("\nVocê sacou $", saque, "de sua conta bancária, seu saldo atual é de: $", saldo)
        menu_inicial()

    else: print ("\nValor insuficiente, seu saldo atual é de $", saldo, "\n")
    sacar()

def exibir_extrato():
    print("\n=======EXTRATO=======\n")
    if len(extrato) == 0:
        print ("Nenhuma movimentação em sua conta... ")
        menu_inicial()

    for i in extrato:
        print (i)

    print ("\n=====================\n")


menu_inicial()