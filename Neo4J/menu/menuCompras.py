
from cadastro.cadastrarCompra import cadastrarCompra
from leitura.leituraCompra import lerCompraPorCPF, lerTodasCompras


def mostrar():
    print("Menu das Compras")   
    print("1 - Cadastrar Compra")
    print("2 - Visualizar Todos as Compras")
    print("3 - Pesquisar Compra por usuário")
    sub = input("Digite a opção desejada: ")
    if (sub == '1'):
        cpf = input("CPF do cliente que fará a compra: ")
        cadastrarCompra(cpf)
            
    elif (sub == '2'):
        print("Buscando todas as Compras... ")
        lerTodasCompras()

    elif (sub == '3'):
        cpf = input("Insira o cpf do usuário que deseja ver as compras: ")
        lerCompraPorCPF(cpf)

    else:
        ("Opção não entendida :(")