from atualizacao.atualizarProduto import atualizarProduto
from cadastro.cadastrarProduto import cadastrarProduto
from exclusao.excluirProduto import excluirProduto
from leitura.leituraProduto import lerProdutosPorNome, lerTodosProdutos


def mostrar():
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