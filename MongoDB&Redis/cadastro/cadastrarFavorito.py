from atualizacao.atualizarFavoritoRedis import atualizarFavoritoRedis
from busca.buscarFavorito import buscarFavoritoPorCPF
from connection import usuariosColecao, produtosColecao

def cadastrarFavorito(cpf):
    global usuariosColecao
    global produtosColecao

    # buscaUsuario = {"cpf": cpf}
    # usuario = usuariosColecao.find_one(buscaUsuario)
    # if usuario == None:
    #     return
    favoritos = buscarFavoritoPorCPF(cpf)

    if favoritos != None:
        resposta = 0
        while (resposta != 'N'):
            nomeProduto = input("Insira o nome do produto que deseja adicionar aos favoritos: ")
            buscaProduto = {"nome": nomeProduto}
            produto = produtosColecao.find_one(buscaProduto)
            if produto != None:
                favoritos.append(produto)
            else:
                print("Produto não encontrado")

            resposta = input("Deseja adicionar mais um produto (S/N)? ").upper()

        atualizarFavoritoRedis(cpf, favoritos)
        print("Favoritos adicionados com sucesso")
    else:
        print("CPF não encontrado")