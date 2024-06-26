from connection import database

def lerCompras(compras):
    listaCompras = {}
    for record in compras:
        idCompra = record["c"]["id"]
        if idCompra not in listaCompras:
            listaCompras[idCompra] = {
                "usuario": record["u"],
                "compra": record["c"],
                "produtos": []
            }
        produto = {
            "nome": record["p"]["nome"],
            "preco": record["p"]["preco"],
            "quantidade": record["quantidade"]
        }
        listaCompras[idCompra]["produtos"].append(produto)
    
    print("Compras existentes: ")
    for idCompra, info_compra in listaCompras.items():
        usuario = info_compra["usuario"]
        compra = info_compra["compra"]
        produtos = info_compra["produtos"]
        
        print(f"Cliente: {usuario['nome']}, CPF: {usuario['cpf']}")
        print(f"Data: {compra['data']}")
        
        print("\nProdutos:")
        for produto in produtos:
            print(f"Qnt:{produto['quantidade']} {produto['nome']} - R${produto['preco'] * produto['quantidade']}")
        
        print(f"Total: {compra['total']}")
        print("-"*50)

        
def lerCompraPorCPF(cpf):
    compras = database.get_compras_por_cpf(cpf)
    if compras != None:
        lerCompras(compras)
    else:
        print("Nenhuma compra encontrada!")

def lerTodasCompras():
    compras = database.get_compras()
    if compras != None:
        lerCompras(compras)
    else:
        print("Nenhuma compra encontrada!")