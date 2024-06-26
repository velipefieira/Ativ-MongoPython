from busca.buscarProduto import buscarProdutosPorNome, buscarProdutoPorId, buscarTodosProdutos
from busca.buscarVendedor import buscarVendedorPorCNPJ, buscarVendedorPorId

def lerProduto(produto):
    print("------------------------------------------")
    print(produto["nome"], "R$",produto["preco"])
    print(produto["descricao"])
    print("Estoque:", produto["estoque"], "Vendas:", produto["vendas"])
    print("Categoria:", produto["categoria"], "\n")
    vendedor = buscarVendedorPorId(produto["id_vendedor"])
    print("Vendedor:", vendedor["nome"], "-", vendedor["cnpj"])

def lerProdutosPorCnpj(cnpj):
    vendedor = buscarVendedorPorCNPJ(cnpj)
    if vendedor == None:
        print("CNPJ não encontrado")
        return
    for prodId in vendedor["id_produtos"]:
        produto = buscarProdutoPorId(prodId)
        lerProduto(produto)

def lerTodosProdutos():
    produtos = buscarTodosProdutos()
    for produto in produtos:
        lerProduto(produto)

def lerProdutosPorNome(nome):
    produtos = buscarProdutosPorNome(nome)
    for produto in produtos:
        lerProduto(produto)
