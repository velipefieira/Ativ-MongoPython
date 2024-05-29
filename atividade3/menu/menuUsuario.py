from atualizacao.atualizarUsuario import atualizarUsuario
from cadastro.cadastrarUsuario import cadastrarUsuario
from exclusao.excluirUsuario import excluirUsuario
from leitura.leituraUsuario import lerTodosUsuarios, lerUsuarioPorCPF

def mostrar():
    print("Menu dos Usuários")
    print("1 - Cadastrar Usuário")
    print("2 - Visualizar Todos os Usuários (MongoDB)")
    print("3 - Visualizar Usuário específico (Redis)")
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