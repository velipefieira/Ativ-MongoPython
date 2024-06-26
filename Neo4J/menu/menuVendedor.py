from cadastro.cadastrarVendedor import cadastrarVendedor
from leitura.leituraVendedor import lerTodosVendedores, lerVendedorPorCNPJ


def mostrar(): 
    print("Menu dos Vendedores")   
    print("1 - Cadastrar Vendedor")
    print("2 - Visualizar Todos os Vendedores")
    print("3 - Visualizar Vendedor específico")
    sub = input("Digite a opção desejada: ")
    if (sub == '1'):
        print("Iniciando cadastro de vendedor...")
        cadastrarVendedor()
            
    elif (sub == '2'):
        print("Buscando todos os vendedores... ")
        lerTodosVendedores()

    elif (sub == '3'):
        cnpj = input("Insira o CNPJ do vendedor para busca: ")
        lerVendedorPorCNPJ(cnpj)
        
    else:
        ("Opção não entendida :(")   