from connection import vendedoresColecao

def buscarTodosVendedores():
    global vendedoresColecao
    vendedores = vendedoresColecao.find().sort("nome")
    return vendedores

def buscarVendedorPorCNPJ(cnpj):
    global vendedoresColecao
    myquery = {"cnpj": cnpj}
    vendedor = vendedoresColecao.find_one(myquery)
    return vendedor

def buscarVendedorPorId(id):
    global vendedoresColecao
    myquery = {"_id": id}
    vendedor = vendedoresColecao.find_one(myquery)
    return vendedor