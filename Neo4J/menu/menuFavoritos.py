
from cadastro.cadastrarFavorito import cadastrarFavorito
from leitura.leituraFavoritos import lerFavoritosPorCPF, lerTodosFavoritos

def mostrar():
    print("Menu dos Favoritos")   
    print("1 - Adicionar um Favorito de um cliente")
    print("2 - Visualizar Todos os Favoritos")
    print("3 - Visualizar Favoritos de um cliente")
    sub = input("Digite a opção desejada: ")
    if (sub == '1'):
        cpf = input("Insira o cpf do cliente que deseja adicionar o Favorito: ")
        cadastrarFavorito(cpf)

    elif (sub == '2'):
        lerTodosFavoritos()

    elif (sub == '3'):
        cpf = input("Insira o cpf do cliente que deseja ver os Favoritos: ")
        lerFavoritosPorCPF(cpf)
    else:
        ("Opção não entendida :(")   