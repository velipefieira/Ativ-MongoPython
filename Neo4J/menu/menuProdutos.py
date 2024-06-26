from cadastro.cadastrarProduto import cadastrarProduto
from leitura.leituraProduto import lerProdutosPorNome, lerTodosProdutos

def mostrar():
    print("Menu dos Produtos")   
    print("1 - Cadastrar Produto")
    print("2 - Visualizar Todos os Produtos")
    print("3 - Pesquisar Produto por nome")
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
    else:
        ("Opção não entendida :(")  