import json
from connection import usuariosColecao, redisDatabase

def buscarFavoritoPorCPF(cpf):
    chave = "favoritos:" + cpf
    favorito = redisDatabase.get(chave)
    if favorito != None:
        favoritoObj = json.loads(favorito)
    else:
        myquery = {"cpf": cpf}
        global usuariosColecao
        usuarioMongo = usuariosColecao.find_one(myquery)
        if usuarioMongo != None:
            favoritoJson = json.dumps(usuarioMongo["favoritos"], default=str)
            redisDatabase.set(chave, favoritoJson)
            listafavoritos = json.loads(favoritoJson)
            return listafavoritos
        else:
            return None
    return favoritoObj