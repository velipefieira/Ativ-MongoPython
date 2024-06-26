from busca.buscarUsuario import buscarTodosUsuarios, buscarUsuarioPorCPF

def lerUsuario(usuario):
    print("---------------------")
    print("Nome:", usuario["nome"], "| CPF:", usuario["cpf"])
    print("Telefone:", usuario["telefone"], "| E-mail:", usuario["email"])
    for endereco in usuario["endereco"]:
        print("Endereço:", endereco["rua"], "n°",endereco["numero"], "| CEP:", endereco["cep"], "Bairro:", endereco["bairro"], "Cidade:", endereco["cidade"], "Estado:", endereco["estado"], "\n")

def lerUsuarioPorCPF(cpf):
    usuario = buscarUsuarioPorCPF(cpf)
    if usuario != None:
        lerUsuario(usuario)
    else:
        print("CPF não encontrado")

def lerTodosUsuarios():
    usuarios = buscarTodosUsuarios()
    for usuario in usuarios:
        lerUsuario(usuario)