from connection import usuariosColecao,comprasColecao
from busca.buscarProduto import buscarUmProdutoPorNome

def excluirCompra(cpf):
    global usuariosColecao
    global comprasColecao

    buscaUsuario = {"cpf": cpf}
    usuario = usuariosColecao.find_one(buscaUsuario)
    if usuario == None:
        print("CPF não encontrado")
        return
    
    buscaCompras = {"id_cliente": usuario["_id"]}
    compras = comprasColecao.find(buscaCompras)

    for compra in compras:
        print("----------------------------------------")
        print("Cliente:", compra["nome"], compra["cpf"])
        print("Data:", compra["data"])
        print("Endereço de entrega:", compra["endereco"])
        print("Produtos:")
        for produto in compra["produtos"]:
            print(produto["nome"], "R$", produto["preco"], "Quantidade:", produto["quantidade"])

        print("Total: R$", compra["total"], "\n")
        excluirCompra = input("Excluir compra? (S/N) ")
        if excluirCompra == "S":
            for produto in compra["produtos"]:
                produtoObj = buscarUmProdutoPorNome(produto["nome"])
                if produtoObj != None:
                    removerVenda(produtoObj["_id"], produto["quantidade"])
            comprasColecao.delete_one(compra)
            print("Deletando a compra")

    busca = {"cliente_cpf": cpf}
    comprasColecao.delete_one(busca)

def removerVenda(produtoId, quantidade):
    global produtosColecao
    buscaProduto = {"_id": produtoId}
    produto = produtosColecao.find_one(buscaProduto)
    produto["vendas"] -= quantidade
    produto["estoque"] += quantidade

    newvalues = { "$set": produto }
    produtosColecao.update_one(buscaProduto, newvalues)