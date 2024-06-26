import json
from connection import redisDatabase

print("setando")
# redisDatabase.set("felipe@gmail.com","felipe testando coisas",30)


# chaves = redisDatabase.keys()
# for chave in chaves:
#         redisDatabase.delete(chave)

obj = redisDatabase.get("Login:345")
print(obj)
print(redisDatabase.keys())


# nome = input("Nome: ")
# sobrenome = input("Sobrenome: ")
# email = input("Email: ")
# end = [] #isso é uma lista

# key = 1

# while (key != 'N'):
#     rua = input("Rua: ")
#     num = input("Num: ")
#     bairro = input("Bairro: ")
#     cidade = input("Cidade: ")
#     estado = input("Estado: ")
#     cep = input("CEP: ")
#     endereco = {        #isso nao eh json, isso é chave-valor, eh um obj
#         "rua":rua,
#         "num": num,
#         "bairro": bairro,
#         "cidade": cidade,
#         "estado": estado,
#         "cep": cep
#     }
#     end.append(endereco) #estou inserindo na lista
#     key = input("Deseja cadastrar um novo endereço (S/N)? ")

# usuario = {  #estou montando o obj final
#     "nome" : nome,
#     "sobrenome" : sobrenome,
#     "email": email,
#     "enderecos" : end
# }

# usuarioobj = json.dumps(usuario)
# print(usuarioobj)
# print("setando")
# redisDatabase.set(usuario["email"], usuarioobj)


# print("lendo")
# obj = json.loads(redisDatabase.get(email))
# print(obj["nome"])
# for x in obj["enderecos"]:
#     print(x)