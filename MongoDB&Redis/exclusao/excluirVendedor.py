from connection import vendedoresColecao, produtosColecao
from busca.buscarVendedor import buscarVendedorPorCNPJ

def excluirVendedor(cnpj):
    global vendedoresColecao
    global produtosColecao
    vendedor = buscarVendedorPorCNPJ(cnpj)
    if vendedor != None:
        for produtoId in vendedor["id_produtos"]:         
            buscaProduto = {"_id": produtoId}    
            produtosColecao.delete_one(buscaProduto)
        
        vendedoresColecao.delete_one(vendedor)
        print("Deletando o vendedor")
    else:
        print("CNPJ não encontrado")