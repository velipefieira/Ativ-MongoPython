from menu import menuCliente, menuVendedor, menuProdutos, menuCompras, menuFavoritos
from connection import database

execucao = True

while execucao:
    key = "x"
    while (key != '0'):
        print("1 - Clientes")
        print("2 - Vendedores")
        print("3 - Produtos")
        print("4 - Compras")
        print("5 - Favoritos")
        print("0 - Sair ")
        key = input("Digite a opção desejada: ")

        if (key == '1'):
            menuCliente.mostrar()    
                    
        elif (key == '2'):
            menuVendedor.mostrar() 

        elif (key == '3'):
            menuProdutos.mostrar()
                    
        elif (key == '4'):
            menuCompras.mostrar()
            
        elif (key == '5'):
            menuFavoritos.mostrar()

        elif (key == "0"):
            print("Tchau tchau...")
            database.close()
            execucao = False

        else:
            print("Opção não entendida :(")