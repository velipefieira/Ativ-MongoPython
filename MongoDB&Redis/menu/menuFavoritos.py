
from cadastro.cadastrarFavorito import cadastrarFavorito
from exclusao.excluirFavorito import excluirFavorito
from leitura.leituraFavoritos import lerFavoritosPorCPF, lerTodosFavoritos


def mostrar():
    print("Menu dos Favoritos")   
    print("1 - Adicionar um Favorito de um cliente")
    print("2 - Visualizar Todos os Favoritos (MongoDB)")
    print("3 - Visualizar Favoritos de um cliente (Redis)")
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
        excluirFavorito(cpf)

    else:
        ("Opção não entendida :(")   