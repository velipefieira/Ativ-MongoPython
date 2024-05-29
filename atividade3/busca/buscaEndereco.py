import json
from connection import usuariosColecao, redisDatabase

def buscarEnderecosPorCPF(cpf):
    chave = "endereco:" + cpf
    endereco = redisDatabase.get(chave)
    if endereco != None:
        enderecoObj = json.loads(endereco)
    else:
        myquery = {"cpf": cpf}
        global usuariosColecao
        usuarioMongo = usuariosColecao.find_one(myquery)
        if usuarioMongo != None:
            enderecoJson = json.dumps(usuarioMongo["endereco"], default=str)
            redisDatabase.set(chave, enderecoJson)
            listaEnderecos = json.loads(enderecoJson)
            return listaEnderecos
        else:
            return None
    return enderecoObj