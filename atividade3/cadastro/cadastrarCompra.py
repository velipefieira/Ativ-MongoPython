from busca.buscarUsuario import buscarUsuarioPorCPF
from connection import comprasColecao, usuariosColecao, produtosColecao
from datetime import datetime

def cadastrarCompra(cpf):
    global comprasColecao
    global usuariosColecao
    global produtosColecao

    buscaUsuario = {"cpf": cpf}
    usuario = buscarUsuarioPorCPF(cpf)
    if usuario == None:
        print("CPF não encontrado")
        return

    produtos = []
    total = 0
    resposta = 0
    while (resposta != 'N'):
        nomeProduto = input("Insira o nome do produto que deseja comprar: ")
        buscaProduto = {"nome": nomeProduto}
        produto = produtosColecao.find_one(buscaProduto)
        if produto != None:
            quantidade = int(input("Insira a quantidade que deseja: "))
            if quantidade <= produto["estoque"]:
                produtoComprado = {"nome": produto["nome"], "preco": produto["preco"], "quantidade": quantidade}
                total += produto["preco"] * quantidade
                produtos.append(produtoComprado)
                adicionarVenda(produto["_id"], quantidade)
            else:
                print("Não foi possível efetuar a compra, estoque insuficiente")
        else:
            print("Produto não encontrado")

        resposta = input("Deseja adicionar mais um produto (S/N)? ").upper()
    
    if produtos == []:
        print("Retornando ao Menu, nenhum produto adicionado. \n")
        return
    
    total = format(total, ".2f")
    data = datetime.now().strftime("%d/%m/%Y")
    resposta = 0

    while (resposta != 'S'):
        for end in usuario["endereco"]:
            if resposta != "S":
                print("Endereço:", end["rua"], "n°",end["numero"], "| CEP:", end["cep"])
                endereco = end
                resposta = input("Deseja enviar para este endereço (S/N)? ").upper()

    compra = {  "produtos": produtos, "total": total, "data": data, "id_cliente": usuario["_id"], "nome": usuario["nome"], "cpf": usuario["cpf"], "endereco": [endereco] }
    x = comprasColecao.insert_one(compra)
    print("Documento inserido com ID ", x.inserted_id)

def adicionarVenda(produtoId, quantidade):
    global produtosColecao
    buscaProduto = {"_id": produtoId}
    produto = produtosColecao.find_one(buscaProduto)
    produto["vendas"] += quantidade
    produto["estoque"] -= quantidade
    
    newvalues = { "$set": produto }
    produtosColecao.update_one(buscaProduto, newvalues)