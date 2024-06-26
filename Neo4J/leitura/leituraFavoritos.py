from connection import database
def lerFavoritos(favoritos):
    listaFavoritos = {}
    
    for record in favoritos:
        idCliente = record["u"]["id"]
        if idCliente not in listaFavoritos:
            listaFavoritos[idCliente] = {
                "usuario": record["u"],
                "produtos": []
            }
        produto = {
            "nome": record["p"]["nome"],
            "descricao": record["p"]["descricao"],
            "preco": record["p"]["preco"]
        }
        listaFavoritos[idCliente]["produtos"].append(produto)
    
    print("Favoritos existentes: ")
    for idCliente, info_compra in listaFavoritos.items():
        usuario = info_compra["usuario"]
        produtos = info_compra["produtos"]

        print(f"Cliente: {usuario['nome']}, CPF: {usuario['cpf']}")        
        print("Favoritos:")
        for produto in produtos:
            print(f"{produto['nome']} - R${produto['preco']}\n{produto['descricao']}")
            
            print("-"*50)

def lerTodosFavoritos():
    favoritos = database.get_favoritos()
    if favoritos != None:
        lerFavoritos(favoritos)

def lerFavoritosPorCPF(cpf):
    usuario = database.get_favoritos_por_cpf(cpf)
    if usuario != None:
        lerFavoritos(usuario)
    else:
        print("CPF não encontrado")