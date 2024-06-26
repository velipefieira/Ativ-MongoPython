from datetime import datetime
from connection import database

def cadastrarUsuario():
    nome = input("Insira o Nome Completo: ")
    email = input("Insira o E-mail: ")
    cpf = input("Insira o CPF: ")
    telefone = input("Insira o telefone: ")

    data_cadastro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    qntUsuarios = database.get_node_count('Usuario')

    idUsuario = qntUsuarios + 1

    cadastroQuery = (
        "CREATE (u:Usuario { id: $id, nome: $nome, email: $email, telefone: $telefone, cpf: $cpf, data_cadastro: $data_cadastro }) RETURN u"
    )

    result = database.query(cadastroQuery, 
        id=idUsuario,
        nome=nome,
        email=email,
        cpf=cpf,
        telefone=telefone,
        data_cadastro=data_cadastro
    )

    if result:
        print("Cliente cadastrado!")
    else:
        print("Erro ao cadastrar cliente.")