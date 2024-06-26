from connection import database

def lerUsuario(usuario):
    print("---------------------")
    print("Nome:", usuario["nome"], "| CPF:", usuario["cpf"])
    print("Telefone:", usuario["telefone"], "| E-mail:", usuario["email"])
    print("Data de cadastro:", usuario['data_cadastro'])

def lerUsuarioPorCPF(cpf):
    usuario = database.get_usuario_por_cpf(cpf)
    if usuario != None:
        lerUsuario(usuario)
    else:
        print("CPF não encontrado")

def lerTodosUsuarios():
    usuarios = database.get_usuarios()
    for usuario in usuarios:
        lerUsuario(usuario)