from datetime import datetime
from connection import database

def cadastrarCompra(cpf):
    idUsuario = database.get_usuario_id_por_cpf(cpf)
    if idUsuario is None:
        print("CPF não encontrado")
        return

    produtos = []
    total = 0.0
    resposta = 'S'
    while resposta != 'N':
        nome = input("Insira o nome do produto que deseja comprar: ")
        idProduto = database.get_produto_id_por_nome(nome)
        if idProduto is not None:
            produto = database.get_produto_por_produto_id(idProduto)
            quantidade = int(input("Insira a quantidade que deseja: "))
            if quantidade <= produto['estoque']:
                produtoComprado = {"id": produto["id"], "nome": produto["nome"], "preco": produto["preco"], "quantidade": quantidade}
                total += produto["preco"] * quantidade
                produtos.append(produtoComprado)
                database.adicionar_venda(produto["id"], quantidade)
            else:
                print("Não foi possível efetuar a compra, estoque insuficiente")
        else:
            print("Produto não encontrado")

        resposta = input("Deseja adicionar mais um produto (S/N)? ").upper()
    
    if not produtos:
        print("Retornando ao Menu, nenhum produto adicionado. \n")
        return

    total = format(total, ".2f")
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    compraQuery = (
        "MATCH (usuario:Usuario {cpf: $cpf}) "
        "CREATE (compra:Compra {id: $idCompra, data: $data, total: $total}) "
        "MERGE (usuario)-[:REALIZA]->(compra) "
        "RETURN compra"
    )

    qntCompras = database.get_node_count('Compra')
    idCompra = qntCompras + 1

    result = database.query(compraQuery,
        cpf=cpf,
        idCompra=idCompra,
        data=data,
        total=total
    )

    if result:
        for produto in produtos:
            produtoCompraQuery = (
                "MATCH (compra:Compra {id: $idCompra}), (produto:Produto {id: $idProduto}) "
                "CREATE (compra)-[:CONTEM {quantidade: $quantidade}]->(produto) "
                "RETURN compra, produto"
            )

            database.query(produtoCompraQuery,
                idCompra=idCompra,
                idProduto=produto['id'],
                quantidade=produto['quantidade']
            )

        print("Compra cadastrada com sucesso!")
    else:
        print("Erro ao cadastrar compra.")