from connection import database

def cadastrarProduto():
    cnpj = input("Insira o CNPJ do vendedor: ")
    Vendedor = database.get_vendedor_por_cnpj(cnpj)

    if Vendedor == None:
        print("CNPJ não encontrado!")
        return
    
    nome = input("Insira o nome do produto: ")
    descricao = input("Insira a descrição do produto: ")
    preco = float(input("Insira o preço do produto (ex: 9.99): "))
    estoque = int(input("Insira o estoque do produto: "))
    qntProdutos = database.get_node_count('Produto')
    idProduto = qntProdutos + 1


    cadastroQuery = (
        "MATCH (vendedor:Vendedor {cnpj: $cnpj}) "
        "CREATE (produto:Produto { id: $idProduto, idVendedor: $idVendedor, nome: $nome, descricao: $descricao, estoque: $estoque, preco: $preco, vendas: $vendas}) "
        "MERGE (vendedor)-[:VENDE]->(produto) "
        "RETURN produto"
    )

    result = database.query(cadastroQuery,
        cnpj=cnpj,
        idProduto=idProduto,
        idVendedor=Vendedor['id'],
        nome=nome,
        descricao=descricao,
        preco=preco,
        estoque=estoque,
        vendas=0
    )

    if result:
        print("Produto cadastrado e vinculado ao vendedor!")
    else:
        print("Erro ao cadastrar produto.")