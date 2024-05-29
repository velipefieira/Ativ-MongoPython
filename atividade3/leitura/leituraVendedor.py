from busca.buscarVendedor import buscarTodosVendedores,buscarVendedorPorCNPJ

def lerVendedor(vendedor):
    print("------------------------------------------")
    print("Nome:", vendedor["nome"])
    print("CNPJ:", vendedor["cnpj"])

def lerVendedorPorCNPJ(cnpj):
    vendedor = buscarVendedorPorCNPJ(cnpj)
    if vendedor != None:
        lerVendedor(vendedor)
    else:
        print("CNPJ não encontrado")
    print()

def lerTodosVendedores():
    print("Vendedores existentes: ")
    vendedores = buscarTodosVendedores()
    for vendedor in vendedores:
        lerVendedor(vendedor)
    print()