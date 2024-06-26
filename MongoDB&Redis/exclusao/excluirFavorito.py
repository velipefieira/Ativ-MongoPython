from atualizacao.atualizarFavoritoRedis import atualizarFavoritoRedis
from busca.buscarFavorito import buscarFavoritoPorCPF
import json

def excluirFavorito(cpf):
    favoritos = buscarFavoritoPorCPF(cpf)

    if favoritos != None:
        novoFavoritos = []
        for favorito in favoritos:
            print(favorito["nome"], "R$",favorito["preco"])
            print(favorito["descricao"])
            excluirFavorito = input("Excluir favorito? (S/N)").upper()
            if excluirFavorito != "S":
                novoFavoritos.append(favorito)

        atualizarFavoritoRedis(cpf, novoFavoritos)
        print("Favoritos atualizados com sucesso")
    else:
        print("CPF não encontrado")