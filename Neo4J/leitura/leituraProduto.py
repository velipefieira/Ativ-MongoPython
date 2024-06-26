from connection import database

def lerProduto(produto):
    print("------------------------------------------")
    print(produto["nome"], "R$",produto["preco"])
    print(produto["descricao"])
    print("Estoque:", produto["estoque"], "Vendas:", produto["vendas"])
    vendedor = database.get_vendedor_por_produto(produto["id"])
    if vendedor != None:
        print("Vendedor:", vendedor["nome"], "-", vendedor["cnpj"])

def lerProdutosPorCnpj(cnpj):
    produto = database.get_produto_por_vendedor(cnpj)
    if produto != None:
        lerProduto(produto)

def lerTodosProdutos():
    produtos = database.get_produtos()
    for produto in produtos:
        lerProduto(produto)

def lerProdutosPorNome(nome):
    produtos = database.get_produto_por_nome(nome)
    for produto in produtos:
        lerProduto(produto)
