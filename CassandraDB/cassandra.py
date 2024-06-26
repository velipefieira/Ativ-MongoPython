# pip install --upgrade astrapy
from astrapy import DataAPIClient
from datetime import datetime

client = DataAPIClient("AstraCS:bziKBdLUEnMFTQSPWmcRiBgb:5dd2ee9af0a77f5c087d7d3b3c18a8c9e07ac12eea41e8fd6b4a238470a7212a")
db = client.get_database_by_api_endpoint(
  "https://ad3241f9-02a1-482f-9711-d4dd5e9c26a1-us-east-2.apps.astra.datastax.com"
)

global comprasColecao
global produtosColecao
global usuariosColecao
global vendedoresColecao

comprasColecao = db.get_collection('compras')
produtosColecao = db.get_collection('produtos')
usuariosColecao = db.get_collection('usuarios')
vendedoresColecao = db.get_collection('vendedor')

# Funções de busca ------------------------------------------

def buscarTodosUsuarios():
    global usuariosColecao
    usuarios = usuariosColecao.find()
    return usuarios

def buscarUsuarioPorCPF(cpf):
    global usuariosColecao
    myquery = {"cpf": cpf}
    usuarios = usuariosColecao.find_one(myquery)
    return usuarios

def buscarUsuarioPorID(id):
    global usuariosColecao
    myquery = {"_id": id}
    usuarios = usuariosColecao.find_one(myquery)
    return usuarios

def buscarTodosVendedores():
    global vendedoresColecao
    vendedores = vendedoresColecao.find()
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

def buscarTodosProdutos():
    global produtosColecao
    produtos = produtosColecao.find()
    return produtos
    
def buscarProdutosPorNome(nome):
    global produtosColecao
    myquery = {"nome": nome}
    produtos = produtosColecao.find(myquery)
    return produtos

def buscarUmProdutoPorNome(nome):
    global produtosColecao
    myquery = {"nome": nome}
    produto = produtosColecao.find_one(myquery)
    return produto

def buscarProdutosPorVendedorId(id):
    global produtosColecao
    myquery = {"id_vendedor": id}
    produtos = produtosColecao.find(myquery)
    return produtos

def buscarProdutoPorId(id):
    global produtosColecao
    myquery = {"_id": id}
    produto = produtosColecao.find_one(myquery)
    return produto

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

# Funções de cadastro ----------------------------------------

def cadastrarUsuario():
    global usuariosColecao
    nome = input("Insira o Nome Completo: ")
    email = input("Insira o E-mail: ")
    cpf = input("Insira o CPF: ")
    telefone = input("Insira o telefone: ")
    key = 1
    end = []
    while (key != 'N'):
        print("Cadastrando um endereço... ")
        rua = input("Insira a Rua: ")
        num = input("Insira o Número: ")
        bairro = input("Insira o Bairro: ")
        cidade = input("Insira a Cidade: ")
        estado = input("Insira o Estado: ")
        cep = input("Insira o CEP: ")
        endereco = {
            "rua":rua,
            "numero": num,
            "bairro": bairro,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        end.append(endereco)
        key = input("Deseja cadastrar um novo endereço (S/N)? ")
        key = key.upper()
    mydoc = { "nome": nome, "email": email, "cpf": cpf, "telefone": telefone, "endereco": end, "data_registro": datetime.now(), "favoritos": [] }
    x = usuariosColecao.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def cadastrarVendedor():
    global vendedoresColecao
    nome = input("Insira o nome do vendedor: ")
    cnpj = input("Insira o CNPJ: ")
    mydoc = {  "nome": nome, "cnpj": cnpj, "id_produtos": [] }
    x = vendedoresColecao.insert_one(mydoc)
    print("Documento inserido com ID ", x.inserted_id)

def cadastrarProduto():
    global produtosColecao
    global vendedoresColecao
    cnpj = input("Insira o CNPJ do vendedor: ")
    myquery = {"cnpj": cnpj}
    vendedor = buscarVendedorPorCNPJ(cnpj)
    if vendedor != None:
        nome = input("Insira o nome do produto: ")
        descricao = input("Insira a descrição do produto: ")
        preco = float(input("Insira o preço do produto (ex: 9.99): "))
        estoque = int(input("Insira o estoque do produto: "))
        categoria = input("Insira o nome da categoria: ")
        mydoc = {  "id_vendedor": vendedor["_id"], "nome": nome, "descricao": descricao, "preco": preco, "estoque": estoque, "vendas": 0, "categoria":categoria }
        x = produtosColecao.insert_one(mydoc)
        vendedor["id_produtos"].append(x.inserted_id)

        if '_id' in vendedor:
            del vendedor['_id']
        
        newvalues = { "$set": vendedor }
        vendedoresColecao.update_one(myquery, newvalues)
        print("Documento inserido com ID ", x.inserted_id)

def cadastrarCompra(cpf):
    global comprasColecao
    global usuariosColecao
    global produtosColecao

    buscaUsuario = {"cpf": cpf}
    usuario = usuariosColecao.find_one(buscaUsuario)
    if usuario == None:
        print("CPF não encontrado")
        return

    produtos = []
    total = 0
    resposta = 0
    while (resposta != 'N'):
        nomeProduto = input("Insira o nome do produto que deseja comprar: ")
        buscaProduto = {"nome": nomeProduto}
        produto = produtosColecao.find_one(buscaProduto)
        if produto != None:
            quantidade = int(input("Insira a quantidade que deseja: "))
            if quantidade <= produto["estoque"]:
                produtoComprado = {"nome": produto["nome"], "preco": produto["preco"], "quantidade": quantidade}
                total += produto["preco"] * quantidade
                produtos.append(produtoComprado)
                adicionarVenda(produto["_id"], quantidade)
            else:
                print("Não foi possível efetuar a compra, estoque insuficiente")
        else:
            print("Produto não encontrado")

        resposta = input("Deseja adicionar mais um produto (S/N)? ")
        resposta = resposta.upper()
    
    if produtos == []:
        print("Retornando ao Menu, nenhum produto adicionado. \n")
        return
    
    total = format(total, ".2f")
    data = datetime.now().strftime("%d/%m/%Y")
    resposta = 0

    while (resposta != 'S'):
        for end in usuario["endereco"]:
            if resposta != "S":
                print("Endereço:", end["rua"], "n°",end["numero"], "| CEP:", end["cep"])
                endereco = end
                resposta = input("Deseja enviar para este endereço (S/N)? ")
                resposta = resposta.upper()

    compra = {  "produtos": produtos, "total": total, "data": data, "id_cliente": usuario["_id"], "nome": usuario["nome"], "cpf": usuario["cpf"], "endereco": [endereco] }
    x = comprasColecao.insert_one(compra)
    print("Documento inserido com ID ", x.inserted_id)


def cadastrarFavorito(cpf):
    global usuariosColecao
    global produtosColecao

    buscaUsuario = {"cpf": cpf}
    usuario = usuariosColecao.find_one(buscaUsuario)
    if usuario == None:
        print("CPF não encontrado")
        return

    favoritos = []
    resposta = 0
    while (resposta != 'N'):
        nomeProduto = input("Insira o nome do produto que deseja adicionar aos favoritos: ")
        buscaProduto = {"nome": nomeProduto}
        produto = produtosColecao.find_one(buscaProduto)
        if produto != None:
            favoritos.append(produto)
        else:
            print("Produto não encontrado")

        resposta = input("Deseja adicionar mais um produto (S/N)? ")
        resposta = resposta.upper()
    
    if favoritos == []:
        print("Retornando ao Menu, nenhum produto adicionado. \n")
        return

    if '_id' in usuario:
        del usuario['_id']
    usuario["favoritos"] = favoritos
    novoUsuario = { "$set": usuario }
    usuariosColecao.update_one(buscaUsuario, novoUsuario)
    print("Favoritos adicionados com sucesso")

# Funções de leitura ----------------------------------------

def lerUsuario(usuario):
    print("---------------------")
    print("Nome:", usuario["nome"], "| CPF:", usuario["cpf"])
    print("Telefone:", usuario["telefone"], "| E-mail:", usuario["email"])
    for endereco in usuario["endereco"]:
            print("Endereço:", endereco["rua"], "n°",endereco["numero"], "| CEP:", endereco["cep"])

def lerUsuarioPorCPF(cpf):
    usuario = buscarUsuarioPorCPF(cpf)
    if usuario != None:
        lerUsuario(usuario)
    else:
        print("CPF não encontrado")

def lerTodosUsuarios():
    usuarios = buscarTodosUsuarios()
    for usuario in usuarios:
        lerUsuario(usuario)
    
def lerVendedor(vendedor):
    print("------------------------------------------")
    print("Nome:", vendedor["nome"])
    print("CNPJ:", vendedor["cnpj"])

def lerVendedorPorCNPJ(cnpj):
    vendedor = buscarVendedorPorCNPJ(cnpj)
    if vendedor != None:
        lerVendedor(vendedor)
    else:
        print("CNPJ não encontrado")
    print()

def lerTodosVendedores():
    print("Vendedores existentes: ")
    vendedores = buscarTodosVendedores()
    for vendedor in vendedores:
        lerVendedor(vendedor)
    print()

def lerProduto(produto):
    print("------------------------------------------")
    print(produto["nome"], "R$",produto["preco"])
    print(produto["descricao"])
    print("Estoque:", produto["estoque"], "Vendas:", produto["vendas"])
    print("Categoria:", produto["categoria"], "\n")
    vendedor = buscarVendedorPorId(produto["id_vendedor"])
    print("Vendedor:", vendedor["nome"], "-", vendedor["cnpj"])

def lerProdutosPorCnpj(cnpj):
    vendedor = buscarVendedorPorCNPJ(cnpj)
    if vendedor == None:
        print("CNPJ não encontrado")
        return
    for prodId in vendedor["id_produtos"]:
        produto = buscarProdutoPorId(prodId)
        lerProduto(produto)

def lerTodosProdutos():
    produtos = buscarTodosProdutos()
    for produto in produtos:
        lerProduto(produto)

def lerProdutosPorNome(nome):
    produtos = buscarProdutosPorNome(nome)
    for produto in produtos:
        lerProduto(produto)

def lerCompras(compras):
    print("Compras existentes: ")
    for compra in compras:
        print("------------------------------------------")
        print("Cliente:", compra["nome"], "CPF:",compra["cpf"])
        print("Data da compra:", compra["data"])
        for endereco in compra["endereco"]:
            print("Endereço de Entrega:", endereco["rua"], "n°",endereco["numero"], "| CEP:", endereco["cep"])
        print("Produtos:")
        for produto in compra["produtos"]:
            print(produto["nome"], "R$", produto["preco"], "Quantidade:", produto["quantidade"])
        print("Total: R$", compra["total"], "\n")
        
def lerCompraPorCPF(cpf):
    compras = buscarComprasPorCPF(cpf)
    lerCompras(compras)

def lerTodasCompras():
    compras = buscarTodasCompras()
    lerCompras(compras)

def lerFavoritos(usuario):
    if usuario["favoritos"] == []:
        return
    else:
        print("------------------------------------------")
        print("Cliente:", usuario["nome"])
        for favorito in usuario["favoritos"]:
            print(favorito["nome"], "R$",favorito["preco"])
            print(favorito["descricao"], "\n")

def lerTodosFavoritos():
    usuarios = buscarTodosUsuarios()
    for usuario in usuarios:
        lerFavoritos(usuario)

def lerFavoritosPorCPF(cpf):
    usuario = buscarUsuarioPorCPF(cpf)
    if usuario != None:
        lerFavoritos(usuario)
    else:
        print("CPF não encontrado")


# Funções de atualização ------------------------------------

def atualizarUsuario(cpf):
    global usuariosColecao
    buscaUsuario = {"cpf": cpf}
    usuario = usuariosColecao.find_one(buscaUsuario)
    if usuario == None:
        print("CPF não encontrado")
        return
    
    compras = buscarComprasPorid(usuario['_id'])
    print("\n Dados do usuário: ")
    print("Nome:", usuario["nome"], "| CPF:", usuario["cpf"])
    print("Telefone:", usuario["telefone"], "| E-mail:", usuario["email"])
    for endereco in usuario["endereco"]:
        print("Endereço:", endereco["rua"], "n°",endereco["numero"], "| CEP:", endereco["cep"], "\n")
    nome = input("Mudar Nome:")
    cpf = input("Mudar CPF:")
    telefone = input("Mudar Telefone:")
    email = input("Mudar E-Mail:")

    if '_id' in usuario:
        del usuario['_id']
    
    if nome:
        usuario["nome"] = nome

    if cpf:
        usuario["cpf"] = cpf

    if telefone:
        usuario["telefone"] = telefone

    if email:
        usuario["email"] = email

    enderecos = []
    for endereco in usuario["endereco"]:
        print("Endereço:", endereco["rua"], "n°",endereco["numero"], "| CEP:", endereco["cep"])
        atualizarEndereco = input("Atualizar endereço? (S/N)")
        if atualizarEndereco == "S":
            rua = input("Insira a Rua: ")
            num = input("Insira o Número: ")
            bairro = input("Insira o Bairro: ")
            cidade = input("Insira a Cidade: ")
            estado = input("Insira o Estado: ")
            cep = input("Insira o CEP: ")
            if rua:
                endereco["rua"] = rua

            if num:
                endereco["num"] = num

            if bairro:
                endereco["bairro"] = bairro

            if estado:
                endereco["estado"] = estado

            if cidade:
                endereco["cidade"] = cidade

            if cep:
                endereco["cep"] = cep
        
        enderecos.append(endereco)

    resposta = 0
    while (True):
        resposta = input("Deseja cadastrar um novo endereço (S/N)? ")
        resposta = resposta.upper()
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

    usuario["endereco"] = enderecos
    novoUsuario = { "$set": usuario }
    usuariosColecao.update_one(buscaUsuario, novoUsuario)
    for compra in compras:
        atualizarDadosCompra(compra)

def atualizarDadosCompra(compra):
    global comprasColecao
    if compra != None:
        usuario = buscarUsuarioPorID(compra["id_cliente"])
        if usuario != None:
            if '_id' in usuario:
                del usuario['_id']

            compra["nome"] = usuario["nome"]
            compra["cpf"] = usuario["cpf"]

            buscaCompra = {"_id": compra['_id']}

            if '_id' in compra:
                del compra['_id']

            novaCompra = { "$set": compra }
            comprasColecao.update_one(buscaCompra, novaCompra)

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

    if '_id' in vendedor:
        del vendedor['_id']

    if len(nome):
        vendedor["nome"] = nome

    cnpj = input("Mudar CNPJ:")
    if len(cnpj):
        vendedor["cnpj"] = cnpj
    
    newvalues = { "$set": vendedor }
    vendedoresColecao.update_one(buscaVendedor, newvalues)

def atualizarProduto(cnpj):
    global vendedoresColecao
    global produtosColecao
    buscaVendedor = {"cnpj": cnpj}
    vendedor = vendedoresColecao.find_one(buscaVendedor)
    if vendedor == None:
        print("CNPJ não encontrado")
        return
    
    for id in vendedor["id_produtos"]:
        buscaProduto = {"_id": id}
        produto = produtosColecao.find_one(buscaProduto)
        print(produto["nome"], "R$",produto["preco"])
        print(produto["descricao"])
        print("Estoque:", produto["estoque"], "Vendas:", produto["vendas"])
        print("Categoria:", produto["categoria"])
        atualizarProduto = input("Atualizar produto? (S/N)")
        if atualizarProduto == "S":
            nome = input("Mudar nome:")

            if '_id' in produto:
                del produto['_id']

            if nome:
                produto["nome"] = nome

            descricao = input("Mudar descrição:")
            if descricao:
                produto["descricao"] = descricao

            preco = input("Mudar preço:")
            if preco:
                produto["preco"] = float(preco)

            estoque = input("Mudar estoque:")
            if estoque:
                produto["estoque"] = int(estoque)

            categoria = input("Mudar categoria:")
            if categoria:
                produto["categoria"] = categoria

            novoProduto = { "$set": produto }
            produtosColecao.update_one(buscaProduto, novoProduto)
            print("Produto alterado com sucesso!")

def adicionarVenda(produtoId, quantidade):
    global produtosColecao
    buscaProduto = {"_id": produtoId}
    produto = produtosColecao.find_one(buscaProduto)
    produto["vendas"] += quantidade
    produto["estoque"] -= quantidade

    if '_id' in produto:
        del produto['_id']
    
    newvalues = { "$set": produto }
    produtosColecao.update_one(buscaProduto, newvalues)

def removerVenda(produtoId, quantidade):
    global produtosColecao
    buscaProduto = {"_id": produtoId}
    produto = produtosColecao.find_one(buscaProduto)
    produto["vendas"] -= quantidade
    produto["estoque"] += quantidade

    if '_id' in produto:
        del produto['_id']

    newvalues = { "$set": produto }
    produtosColecao.update_one(buscaProduto, newvalues)

#Funções de exclusão ----------------------------------------

def excluirUsuario(cpf):
    global usuariosColecao
    myquery = {"cpf": cpf}
    print("Deletando o usuário")
    usuariosColecao.delete_one(myquery)

def excluirVendedor(cnpj):
    global vendedoresColecao
    global produtosColecao
    vendedor = buscarVendedorPorCNPJ(cnpj)
    buscaVendedor = { 'cnpj': cnpj}
    if vendedor != None:
        for produtoId in vendedor["id_produtos"]:         
            buscaProduto = {"_id": produtoId}    
            produtosColecao.delete_one(buscaProduto)
        
        vendedoresColecao.delete_one(buscaVendedor)
        print("Deletando o vendedor")
    else:
        print("CNPJ não encontrado")

def excluirProduto(cnpj):
    global produtosColecao
    global vendedoresColecao

    buscaVendedor = {"cnpj": cnpj}
    vendedor = vendedoresColecao.find_one(buscaVendedor)
    if vendedor == None:
        print("CNPJ não encontrado")
        return
    
    for id in vendedor["id_produtos"]:
        buscaProduto = {"_id": id}
        produto = produtosColecao.find_one(buscaProduto)
        print(produto["nome"], "R$",produto["preco"])
        print(produto["descricao"])
        print("Estoque:", produto["estoque"], "Vendas:", produto["vendas"])
        print("Categoria:", produto["categoria"])
        excluirProduto = input("Excluir produto? (S/N)")
        if excluirProduto == "S":
            print("Deletando o produto")
            produtosColecao.delete_one(buscaProduto)

def excluirFavoritos(cpf):
    global usuariosColecao
    buscaUsuario = {"cpf": cpf}
    usuario = usuariosColecao.find_one(buscaUsuario)
    if usuario == None:
        print("CPF não encontrado")
        return
    
    favoritos = []
    for favorito in usuario["favoritos"]:
        print(favorito["nome"], "R$",favorito["preco"])
        print(favorito["descricao"])
        excluirFavorito = input("Excluir favorito? (S/N)")
        if excluirFavorito != "S":
            favoritos.append(favorito)

    if '_id' in usuario:
        del usuario['_id']
    usuario["favoritos"] = favoritos
    novoUsuario = { "$set": usuario }
    usuariosColecao.update_one(buscaUsuario, novoUsuario)
    print("Favoritos atualizados com sucesso")
    

def excluirCompra(cpf):
    global usuariosColecao
    global comprasColecao

    buscaUsuario = {"cpf": cpf}
    usuario = usuariosColecao.find_one(buscaUsuario)
    if usuario == None:
        print("CPF não encontrado")
        return
    
    buscaCompras = {"id_cliente": usuario["_id"]}
    compras = comprasColecao.find(buscaCompras)

    for compra in compras:
        buscaCompras = { '_id': compra['_id'] }
        print("----------------------------------------")
        print("Cliente:", compra["nome"], compra["cpf"])
        print("Data:", compra["data"])
        print("Endereço de entrega:", compra["endereco"])
        print("Produtos:")
        for produto in compra["produtos"]:
            print(produto["nome"], "R$", produto["preco"], "Quantidade:", produto["quantidade"])

        print("Total: R$", compra["total"], "\n")
        excluirCompra = input("Excluir compra? (S/N) ")
        if excluirCompra == "S":
            for produto in compra["produtos"]:
                produtoObj = buscarUmProdutoPorNome(produto["nome"])
                if produtoObj != None:
                    removerVenda(produtoObj["_id"], produto["quantidade"])
            comprasColecao.delete_one(buscaCompras)
            print("Deletando a compra")

    busca = {"cliente_cpf": cpf}
    comprasColecao.delete_one(busca)


# Menu de navegação 
key = 0
sub = 0
while (key != '0'):
    print("1 - Usuários")
    print("2 - Vendedores")
    print("3 - Produtos")
    print("4 - Compras")
    print("5 - Favoritos")
    print("0 - Sair ")
    key = input("Digite a opção desejada: ")

    if (key == '1'):
        print("Menu dos Usuários")
        print("1 - Cadastrar Usuário")
        print("2 - Visualizar Todos os Usuários")
        print("3 - Visualizar Usuário específico")
        print("4 - Atualizar Usuário")
        print("5 - Excluir Usuário")
        sub = input("Digite a opção desejada: ")
        if (sub == '1'):
            print("Iniciando cadastro de usuario...")
            cadastrarUsuario()
            
        elif (sub == '2'):
            print("Buscando todos os usuários... ")
            lerTodosUsuarios()

        elif (sub == '3'):
            cpf = input("Insira o CPF do cliente para busca: ")
            lerUsuarioPorCPF(cpf)
        
        elif (sub == '4'):
            cpf = input("CPF do usuário que será atualizado: ")
            atualizarUsuario(cpf)

        elif (sub == '5'):
            print("Iniciando exclusão de usuário... ")
            cpf = input("CPF do usuário a ser excluido: ")
            excluirUsuario(cpf)   
        else:
            ("Opção não entendida :(")            
            
    elif (key == '2'):
        print("Menu dos Vendedores")   
        print("1 - Cadastrar Vendedor")
        print("2 - Visualizar Todos os Vendedores")
        print("3 - Visualizar Vendedor específico")
        print("4 - Atualizar Vendedor")
        print("5 - Excluir Vendedor")
        sub = input("Digite a opção desejada: ")
        if (sub == '1'):
            print("Iniciando cadastro de vendedor...")
            cadastrarVendedor()
            
        elif (sub == '2'):
            print("Buscando todos os vendedores... ")
            lerTodosVendedores()

        elif (sub == '3'):
            cnpj = input("Insira o CNPJ do vendedor para busca: ")
            lerVendedorPorCNPJ(cnpj)
        
        elif (sub == '4'):
            cnpj = input("CNPJ do vendedor que será atualizado: ")
            atualizarVendedor(cnpj)

        elif (sub == '5'):
            print("Iniciando exclusão de vendedor... ")
            cnpj = input("CNPJ do vendedor a ser excluido: ")
            excluirVendedor(cnpj)
        else:
            ("Opção não entendida :(")    

    elif (key == '3'):
        print("Menu dos Produtos")   
        print("1 - Cadastrar Produto")
        print("2 - Visualizar Todos os Produtos")
        print("3 - Pesquisar Produto por nome")
        print("4 - Atualizar Produto")
        print("5 - Excluir Produto")
        sub = input("Digite a opção desejada: ")
        if (sub == '1'):
            print("Iniciando cadastro de produto...")
            cadastrarProduto()
            
        elif (sub == '2'):
            print("Buscando todos os produtos... ")
            lerTodosProdutos()

        elif (sub == '3'):
            nome = input("Insira o nome do produto para busca: ")
            lerProdutosPorNome(nome)
        
        elif (sub == '4'):
            cnpj = input("CNPJ do responsável pelo produto que será atualizado: ")
            atualizarProduto(cnpj)

        elif (sub == '5'):
            cnpj = input("CNPJ do vendedor responsável pelo produto a ser excluido: ")
            excluirProduto(cnpj)
        else:
            ("Opção não entendida :(")    
            
    elif (key == '4'):
        print("Menu das Compras")   
        print("1 - Cadastrar Compra")
        print("2 - Visualizar Todos as Compras")
        print("3 - Pesquisar Compra por usuário")
        print("4 - Excluir Compra")
        sub = input("Digite a opção desejada: ")
        if (sub == '1'):
            cpf = input("CPF do cliente que fará a compra: ")
            cadastrarCompra(cpf)
            
        elif (sub == '2'):
            print("Buscando todas as Compras... ")
            lerTodasCompras()

        elif (sub == '3'):
            cpf = input("Insira o cpf do usuário que deseja ver as compras: ")
            lerCompraPorCPF(cpf)

        elif (sub == '4'):
            cpf = input("Insira o cpf do usuário que deseja excluir uma compra: ")
            excluirCompra(cpf)
        else:
            ("Opção não entendida :(")  
    
    elif (key == '5'):
        print("Menu dos Favoritos")   
        print("1 - Adicionar um Favorito de um cliente")
        print("2 - Visualizar Todos os Favoritos")
        print("3 - Visualizar Favoritos de um cliente")
        print("4 - Remover um Favorito de um cliente")
        sub = input("Digite a opção desejada: ")
        if (sub == '1'):
            cpf = input("Insira o cpf do cliente que deseja adicionar o Favorito: ")
            cadastrarFavorito(cpf)

        elif (sub == '2'):
            print("Buscando todos os favoritos... ")
            lerTodosFavoritos()

        elif (sub == '3'):
            cpf = input("Insira o cpf do cliente que deseja ver os Favoritos: ")
            lerFavoritosPorCPF(cpf)

        elif (sub == '4'):
            cpf = input("Insira o cpf do cliente que deseja excluir um Favorito: ")
            excluirFavoritos(cpf)

        else:
            ("Opção não entendida :(")   

    elif (key != "0"):
        print("Opção não entendida :(")

print("Tchau tchau...")