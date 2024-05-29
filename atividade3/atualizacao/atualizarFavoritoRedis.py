from connection import redisDatabase
import json

def atualizarFavoritoRedis(cpf, favoritos):
    chave = "favoritos:" + cpf
    favoritoJson = json.dumps(favoritos, default=str)
    redisDatabase.set(chave, favoritoJson)