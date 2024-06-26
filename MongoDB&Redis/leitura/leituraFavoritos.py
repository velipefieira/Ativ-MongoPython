from busca.buscarUsuario import buscarTodosUsuarios, buscarUsuarioPorCPF

def lerFavoritos(usuario):
    if usuario["favoritos"] == []:
        return
    else:
        print("------------------------------------------")
        print("Cliente:", usuario["nome"])
        for favorito in usuario["favoritos"]:
            print(favorito["nome"], "R$",favorito["preco"])
            print(favorito["descricao"], "\n")

def lerTodosFavoritos():
    usuarios = buscarTodosUsuarios()
    for usuario in usuarios:
        lerFavoritos(usuario)

def lerFavoritosPorCPF(cpf):
    usuario = buscarUsuarioPorCPF(cpf)
    if usuario != None:
        lerFavoritos(usuario)
    else:
        print("CPF não encontrado")