from connection import vendedoresColecao, produtosColecao

def excluirProduto(cnpj):
    global produtosColecao
    global vendedoresColecao

    buscaVendedor = {"cnpj": cnpj}
    vendedor = vendedoresColecao.find_one(buscaVendedor)
    if vendedor == None:
        print("CNPJ não encontrado")
        return
    
    for id in vendedor["id_produtos"]:
        buscaProduto = {"_id": id}
        produto = produtosColecao.find_one(buscaProduto)
        print(produto["nome"], "R$",produto["preco"])
        print(produto["descricao"])
        print("Estoque:", produto["estoque"], "Vendas:", produto["vendas"])
        print("Categoria:", produto["categoria"])
        excluirProduto = input("Excluir produto? (S/N)")
        if excluirProduto == "S":
            print("Deletando o produto")
            produtosColecao.delete_one(produto)