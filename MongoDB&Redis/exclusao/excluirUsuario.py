from connection import usuariosColecao

def excluirUsuario(cpf):
    myquery = {"cpf": cpf}
    global usuariosColecao
    usuariosColecao.delete_one(myquery)
