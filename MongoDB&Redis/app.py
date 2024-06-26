import json
from busca.buscaEndereco import buscarEnderecosPorCPF
from busca.buscarFavorito import buscarFavoritoPorCPF
from busca.buscarUsuario import buscarTodosUsuarios, buscarUsuarioPorCPF
from connection import redisDatabase
from menu import menuUsuario, menuVendedor, menuProdutos, menuCompras, menuFavoritos
import autorizacao
from vincularRedis import vincularRedis

execucao = True
autenticacao = False

while execucao:
    if not autenticacao:
        print("------------------------------------------")
        print("\n Bem-Vindo ao Mercado Livre! \n")
        cpf = input("Insira o seu CPF: ")
        usuario = buscarUsuarioPorCPF(cpf)
        if usuario != None:
            chave = "Login:" + usuario["cpf"]
            usuarioObj = json.dumps(usuario, default=str)
            # redisDatabase.set(chave, usuarioObj, 3600)
            redisDatabase.set(chave, usuarioObj, 60)
            # buscarTodosUsuarios()
            autenticacao = True
        else:
            print("CPF não encontrado :(")
    else:
        key = "x"
        while (key != '0' and autenticacao == True):
            print("1 - Usuários")
            print("2 - Vendedores")
            print("3 - Produtos")
            print("4 - Compras")
            print("5 - Favoritos")
            print("0 - Sair ")
            key = input("Digite a opção desejada: ")

            if (key == '1'):
                menuUsuario.mostrar()          
                    
            elif (key == '2'):
                menuVendedor.mostrar() 

            elif (key == '3'):
                menuProdutos.mostrar()
                    
            elif (key == '4'):
                menuCompras.mostrar()
            
            elif (key == '5'):
                menuFavoritos.mostrar()

            elif (key == "0"):
                vincularRedis()
                print("Tchau tchau...")
                execucao = False

            else:
                print("Opção não entendida :(")
            
            autenticacao = autorizacao.verificar("Login:" + usuario["cpf"])
