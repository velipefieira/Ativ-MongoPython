from connection import produtosColecao, vendedoresColecao

def cadastrarProduto():
    global produtosColecao
    global vendedoresColecao
    cnpj = input("Insira o CNPJ do vendedor: ")
    myquery = {"cnpj": cnpj}
    vendedor = vendedoresColecao.find(myquery)
    for vend in vendedor:
        nome = input("Insira o nome do produto: ")
        descricao = input("Insira a descrição do produto: ")
        preco = float(input("Insira o preço do produto (ex: 9.99): "))
        estoque = int(input("Insira o estoque do produto: "))
        categoria = input("Insira o nome da categoria: ")
        mydoc = {  "id_vendedor": vend["_id"], "nome": nome, "descricao": descricao, "preco": preco, "estoque": estoque, "vendas": 0, "categoria":categoria }
        x = produtosColecao.insert_one(mydoc)
        vend["id_produtos"].append(x.inserted_id)
        newvalues = { "$set": vend }
        vendedoresColecao.update_one(myquery, newvalues)
        print("Documento inserido com ID ", x.inserted_id)