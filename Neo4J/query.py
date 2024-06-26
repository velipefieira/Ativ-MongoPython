add_user_query = """
CREATE (u:Usuario {nome: $nome})
RETURN u
"""

add_cliente_query = """
CREATE (c:Cliente {nome: $nome})
RETURN c
"""

add_vendedor_query = """
CREATE (v:Vendedor {nome: $nome})
RETURN v
"""

add_produto_query = """
CREATE (p:Produto {nome: $nome, preco: $preco})
RETURN p
"""

add_endereco_query = """
CREATE (e:Endereco {endereco: $endereco})
RETURN e
"""

add_compra_query = """
CREATE (co:Compra {id: $id})
RETURN co
"""

add_favorito_query = """
CREATE (f:Favorito {id: $id})
RETURN f
"""

add_relacionomento_query = """
MATCH (a:Usuario {nome: $nomeA}), (b:{labelB} {nome: $nomeB})
CREATE (a)-[r:{relationship}]->(b)
RETURN r
"""