from connection import vendedoresColecao, produtosColecao

def atualizarProduto(cnpj):
    global vendedoresColecao
    global produtosColecao
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
        atualizarProduto = input("Atualizar produto? (S/N)").upper()
        if atualizarProduto == "S":
            nome = input("Mudar nome:")
            if nome:
                produto["nome"] = nome

            descricao = input("Mudar descrição:")
            if descricao:
                produto["descricao"] = descricao

            preco = input("Mudar preço:")
            if preco:
                produto["preco"] = float(preco)

            estoque = input("Mudar estoque:")
            if estoque:
                produto["estoque"] = int(estoque)

            categoria = input("Mudar categoria:")
            if categoria:
                produto["categoria"] = categoria

            novoProduto = { "$set": produto }
            produtosColecao.update_one(buscaProduto, novoProduto)
            print("Produto alterado com sucesso!")