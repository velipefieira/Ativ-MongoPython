from connection import database

def cadastrarFavorito(cpf):
    idUsuario = database.get_usuario_por_cpf(cpf)
    if idUsuario != None:
        resposta = 0
        while (resposta != 'N'):
            nome = input("Insira o nome do produto que deseja adicionar aos favoritos: ")
            idProduto = database.get_produto_por_nome(nome)
            if idProduto != None:
                cadastroQuery = (
                    "MATCH (usuario:Usuario {cpf: $cpf}) "
                    "MATCH (produto:Produto {nome: $nome}) "
                    "MERGE (usuario)-[:FAVORITOU]->(produto) "
                    "RETURN produto"
                )

                result = database.query(cadastroQuery,
                    cpf=cpf,
                    nome=nome
                )

                if result:
                    print("Favorito cadastrado com sucesso!")
                else:
                    print("Erro ao favoritar produto.")
            else:
                print("Produto não encontrado!")

            resposta = input("Deseja adicionar mais um produto (S/N)? ").upper()
    else:
        print("CPF não encontrado")