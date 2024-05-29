from atualizacao.atualizarVendedor import atualizarVendedor
from cadastro.cadastrarVendedor import cadastrarVendedor
from exclusao.excluirVendedor import excluirVendedor
from leitura.leituraVendedor import lerTodosVendedores, lerVendedorPorCNPJ


def mostrar(): 
    print("Menu dos Vendedores")   
    print("1 - Cadastrar Vendedor")
    print("2 - Visualizar Todos os Vendedores")
    print("3 - Visualizar Vendedor específico")
    print("4 - Atualizar Vendedor")
    print("5 - Excluir Vendedor")
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
        
    elif (sub == '4'):
        cnpj = input("CNPJ do vendedor que será atualizado: ")
        atualizarVendedor(cnpj)

    elif (sub == '5'):
        print("Iniciando exclusão de vendedor... ")
        cnpj = input("CNPJ do vendedor a ser excluido: ")
        excluirVendedor(cnpj)
        
    else:
        ("Opção não entendida :(")   