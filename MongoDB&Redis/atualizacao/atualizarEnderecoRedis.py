from connection import redisDatabase
import json

def atualizarEnderecoRedis(cpf, enderecos):
    chave = "endereco:" + cpf
    enderecoJson = json.dumps(enderecos, default=str)
    redisDatabase.set(chave, enderecoJson)