from atualizacao.atualizarEnderecoRedis import atualizarEnderecoRedis
from busca.buscarCompra import buscarComprasPorid
from busca.buscarUsuario import buscarUsuarioPorCPF, buscarUsuarioPorID
from connection import usuariosColecao, comprasColecao

def atualizarUsuario(cpf):
    usuario = buscarUsuarioPorCPF(cpf)
    if usuario == None:
        print("CPF não encontrado")
        return
    
    usuario
    print("\n Dados do usuário: ")
    print("Nome:", usuario["nome"], "| CPF:", usuario["cpf"])
    print("Telefone:", usuario["telefone"], "| E-mail:", usuario["email"])
    for endereco in usuario["endereco"]:
        print("Endereço:", endereco["rua"], "n°",endereco["numero"], "| CEP:", endereco["cep"], "Bairro:", endereco["bairro"], "Cidade:", endereco["cidade"], "Estado:", endereco["estado"], "\n")
    nome = input("Mudar Nome:")
    cpf = input("Mudar CPF:")
    telefone = input("Mudar Telefone:")
    email = input("Mudar E-Mail:")
    
    usuarioNovo = {}
    if nome:
        usuarioNovo["nome"] = nome

    if cpf:
        usuarioNovo["cpf"] = cpf

    if telefone:
        usuarioNovo["telefone"] = telefone

    if email:
        usuarioNovo["email"] = email

    enderecos = []
    for endereco in usuario["endereco"]:
        print("Endereço:", endereco["rua"], "n°",endereco["numero"], "| CEP:", endereco["cep"])
        atualizarEndereco = input("Atualizar endereço? (S/N)").upper()
        if atualizarEndereco == "S":
            rua = input("Mudar a Rua: ")
            numero = input("Mudar o Número: ")
            bairro = input("Mudar o Bairro: ")
            cidade = input("Mudar a Cidade: ")
            estado = input("Mudar o Estado: ")
            cep = input("Mudar o CEP: ")
            enderecoNovo = {}

            if rua:
                enderecoNovo["rua"] = rua
            else:
                enderecoNovo["rua"] = endereco["rua"]
            if numero:
                enderecoNovo["numero"] = numero
            else:
                enderecoNovo["numero"] = endereco["numero"]
            if bairro:
                enderecoNovo["bairro"] = bairro
            else:
                enderecoNovo["bairro"] = endereco["bairro"]
            if cidade:
                enderecoNovo["cidade"] = cidade
            else:
                enderecoNovo["cidade"] = endereco["cidade"]
            if estado:
                enderecoNovo["estado"] = estado
            else:
                enderecoNovo["estado"] = endereco["estado"]
            if cep:
                enderecoNovo["cep"] = cep
            else:
                enderecoNovo["cep"] = endereco["cep"]

            enderecos.append(enderecoNovo)
        else:
            enderecos.append(endereco)

    resposta = 0
    while (True):
        resposta = input("Deseja cadastrar um novo endereço (S/N)? ").upper()
        if resposta == "S":
            print("Cadastrando um endereço... ")
            rua = input("Insira a Rua: ")
            num = input("Insira o Número: ")
            bairro = input("Insira o Bairro: ")
            cidade = input("Insira a Cidade: ")
            estado = input("Insira o Estado: ")
            cep = input("Insira o CEP: ")
            enderecoNovo = {
                "rua":rua,
                "numero": num,
                "bairro": bairro,
                "cidade": cidade,
                "estado": estado,
                "cep": cep
            }
            enderecos.append(enderecoNovo)
        else:
            break

    # usuarioNovo["endereco"] = enderecos
    atualizarEnderecoRedis(usuario["cpf"], enderecos)
    usuarioNovo = { "$set": usuarioNovo }
    busca = { "cpf": usuario["cpf"]}
    usuariosColecao.update_one(busca, usuarioNovo)

    compras = buscarComprasPorid(usuario["_id"])
    for compra in compras:
        atualizarDadosCompra(compra)

def atualizarDadosCompra(compraAntiga):
    global comprasColecao
    compra = comprasColecao.find_one(compraAntiga)
    if compra != None:
        usuario = buscarUsuarioPorID(compra["id_cliente"])
        if usuario != None:
            compra["nome"] = usuario["nome"]
            compra["cpf"] = usuario["cpf"]
            novaCompra = { "$set": compra }
            comprasColecao.update_one(compraAntiga, novaCompra)