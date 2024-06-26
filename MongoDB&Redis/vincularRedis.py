import json
from connection import usuariosColecao, redisDatabase

def vincularRedis():
    global usuariosColecao
    chaves = redisDatabase.keys()
    print("Vinculando o Redis com o MongoDB")
    for chave in chaves:
        objeto = redisDatabase.get(chave)
        objeto = json.loads(objeto)
        chaveDecode = chave.decode('utf-8').split(":")
        if chaveDecode[0] == "favoritos" or chaveDecode[0] == "endereco":
            busca = {"cpf": chaveDecode[1]}
            usuario = usuariosColecao.find_one(busca)
            if usuario != None:
                usuario[chaveDecode[0]] = objeto
                usuarioNovo = { "$set": usuario }
                usuariosColecao.update_one(busca, usuarioNovo)
            redisDatabase.delete(chave)
