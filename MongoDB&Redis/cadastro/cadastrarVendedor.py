from connection import vendedoresColecao

def cadastrarVendedor():
    global vendedoresColecao
    nome = input("Insira o nome do vendedor: ")
    cnpj = input("Insira o CNPJ: ")
    mydoc = {  "nome": nome, "cnpj": cnpj, "id_produtos": [] }
    x = vendedoresColecao.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)