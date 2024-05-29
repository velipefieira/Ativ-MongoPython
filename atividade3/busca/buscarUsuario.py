import json
from busca.buscaEndereco import buscarEnderecosPorCPF
from busca.buscarFavorito import buscarFavoritoPorCPF
from connection import usuariosColecao, redisDatabase

def buscarTodosUsuarios():
    global usuariosColecao
    usuarios = usuariosColecao.find().sort("nome")
    return usuarios

def buscarUsuarioPorCPF(cpf):
    myquery = {"cpf": cpf}
    global usuariosColecao
    usuario = usuariosColecao.find_one(myquery)
    if usuario != None:
        enderecos = buscarEnderecosPorCPF(cpf)
        if enderecos != None:
            usuario["endereco"] = enderecos

        favoritos = buscarFavoritoPorCPF(cpf)
        if favoritos != None:
            usuario["favoritos"] = favoritos
        
        return usuario
    else:
        return None

def buscarUsuarioPorID(id):
    global usuariosColecao
    myquery = {"_id": id}
    usuarios = usuariosColecao.find_one(myquery)
    return usuarios

