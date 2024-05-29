from connection import vendedoresColecao

def atualizarVendedor(cnpj):
    global vendedoresColecao
    buscaVendedor = {"cnpj": cnpj}
    vendedor = vendedoresColecao.find_one(buscaVendedor)
    if vendedor == None:
        print("CNPJ não encontrado")
        return
    
    print("\n Deixe o campo vazio para não alterar.")
    print("Dados do usuário: ")
    print("Nome:", vendedor["nome"], "| CNPJ:", vendedor["cnpj"])
    nome = input("Mudar Nome:")
    if len(nome):
        vendedor["nome"] = nome

    cnpj = input("Mudar CNPJ:")
    if len(cnpj):
        vendedor["cnpj"] = cnpj
    
    newvalues = { "$set": vendedor }
    vendedoresColecao.update_one(buscaVendedor, newvalues)