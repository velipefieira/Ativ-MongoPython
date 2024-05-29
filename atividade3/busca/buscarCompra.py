from busca.buscarUsuario import buscarUsuarioPorCPF
from connection import comprasColecao, usuariosColecao

def buscarTodasCompras():
    global comprasColecao
    compras = comprasColecao.find()
    return compras

def buscarComprasPorCPF(cpf):
    global comprasColecao
    global usuariosColecao
    usuario = buscarUsuarioPorCPF(cpf)
    if usuario != None:
        buscaCompras = {"id_cliente": usuario["_id"]}
        compras = comprasColecao.find(buscaCompras)
        return compras
    else:
        return []
    
def buscarComprasPorid(id):
    global comprasColecao
    global usuariosColecao
    buscaCompras = {"id_cliente": id}
    compras = comprasColecao.find(buscaCompras)
    return compras