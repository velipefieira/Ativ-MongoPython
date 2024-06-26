from connection import database

def lerVendedor(vendedor):
    print("------------------------------------------")
    print("Nome:", vendedor["nome"])
    print("CNPJ:", vendedor["cnpj"])

def lerVendedorPorCNPJ(cnpj):
    vendedor = database.get_vendedor_por_cnpj(cnpj)
    if vendedor != None:
        lerVendedor(vendedor)
    else:
        print("CNPJ não encontrado")
    print()

def lerTodosVendedores():
    print("Vendedores existentes: ")
    vendedores = database.get_vendedores()
    for vendedor in vendedores:
        lerVendedor(vendedor)
    print()