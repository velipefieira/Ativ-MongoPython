from busca.buscarCompra import buscarComprasPorCPF, buscarTodasCompras

def lerCompras(compras):
    print("Compras existentes: ")
    for compra in compras:
        print("------------------------------------------")
        print("Cliente:", compra["nome"], "CPF:",compra["cpf"])
        print("Data da compra:", compra["data"])
        for endereco in compra["endereco"]:
            print("Endereço de Entrega:", endereco["rua"], "n°",endereco["numero"], "| CEP:", endereco["cep"])
        print("Produtos:")
        for produto in compra["produtos"]:
            print(produto["nome"], "R$", produto["preco"], "Quantidade:", produto["quantidade"])
        print("Total: R$", compra["total"], "\n")
        
def lerCompraPorCPF(cpf):
    compras = buscarComprasPorCPF(cpf)
    lerCompras(compras)

def lerTodasCompras():
    compras = buscarTodasCompras()
    lerCompras(compras)