from cadastro.cadastrarUsuario import cadastrarUsuario
from leitura.leituraUsuario import lerTodosUsuarios, lerUsuarioPorCPF

def mostrar():
    print("Menu dos Usuários")
    print("1 - Cadastrar Usuário")
    print("2 - Visualizar Todos os Usuários")
    print("3 - Visualizar Usuário específico")
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
    else:
        ("Opção não entendida :(") 