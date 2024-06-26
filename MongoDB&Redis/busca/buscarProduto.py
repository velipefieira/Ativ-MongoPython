from connection import produtosColecao

def buscarTodosProdutos():
    global produtosColecao
    produtos = produtosColecao.find().sort("nome")
    return produtos
    
def buscarProdutosPorNome(nome):
    global produtosColecao
    myquery = {"nome": nome}
    produtos = produtosColecao.find(myquery)
    return produtos

def buscarUmProdutoPorNome(nome):
    global produtosColecao
    myquery = {"nome": nome}
    produto = produtosColecao.find_one(myquery)
    return produto

def buscarProdutosPorVendedorId(id):
    global produtosColecao
    myquery = {"id_vendedor": id}
    produtos = produtosColecao.find(myquery)
    return produtos

def buscarProdutoPorId(id):
    global produtosColecao
    myquery = {"_id": id}
    produto = produtosColecao.find_one(myquery)
    return produto