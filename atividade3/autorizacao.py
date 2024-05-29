from connection import redisDatabase
from vincularRedis import vincularRedis

def verificar(chave):
    data = redisDatabase.get(chave)
    if data != None:
        return True
    else:
        print("Sua sessão expirou, tente fazer login novamente!")
        vincularRedis()
        return False
