from datetime import datetime
import json
from connection import usuariosColecao, redisDatabase

def cadastrarUsuario():
    global usuariosColecao
    nome = input("Insira o Nome Completo: ")
    email = input("Insira o E-mail: ")
    cpf = input("Insira o CPF: ")
    telefone = input("Insira o telefone: ")
    key = 1
    end = []
    while (key != 'N'):
        print("Cadastrando um endereço... ")
        rua = input("Insira a Rua: ")
        num = input("Insira o Número: ")
        bairro = input("Insira o Bairro: ")
        cidade = input("Insira a Cidade: ")
        estado = input("Insira o Estado: ")
        cep = input("Insira o CEP: ")
        endereco = {
            "rua":rua,
            "numero": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco)
        key = input("Deseja cadastrar um novo endereço (S/N)? ").upper()

    mydoc = { "nome": nome, "email": email, "cpf": cpf, "telefone": telefone, "endereco": end, "data_registro": datetime.now(), "favoritos": [] }
    x = usuariosColecao.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)