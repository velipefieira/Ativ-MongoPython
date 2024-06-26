# pip install neo4j

from neo4j import GraphDatabase

class Neo4jConnection:

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()
    
    def get_produto_por_nome(self, nome):
        query = (
            "MATCH (p:Produto {nome: $nome}) "
            "RETURN p as p"
        )
        result = self.query(query, nome=nome)
        return result[0]['p'] if result else None
    
    def get_vendedor_por_produto(self, id):
        query = (
            "MATCH (v:Vendedor)-[:VENDE]->(p:Produto {id: $id}) "
            "RETURN v as v"
        )
        result = self.query(query, id=id)
        return result[0]['v'] if result else None
    
    def get_produto_por_vendedor(self, cnpj):
        query = (
            "MATCH (v:Vendedor{cnpj: $cnpj})-[:VENDE]->p:Produto) "
            "RETURN p as p"
        )
        result = self.query(query, cnpj=cnpj)
        return result if result else None
    
    def get_produto_por_produto_id(self, idProduto):
        query = """
            MATCH (p:Produto {id: $idProduto})
            RETURN p as p
        """
        result = self.query(query, idProduto=idProduto)
        return result[0]['p'] if result else None
    
    def get_produtos(self):
        query = "MATCH (p:Produto) RETURN p"
        result = self.query(query)
        return [record["p"] for record in result]
    
    def get_usuarios(self):
        query = "MATCH (u:Usuario) RETURN u"
        result = self.query(query)
        return [record["u"] for record in result]
    
    def get_usuario_por_cpf(self, cpf):
        query = (
            "MATCH (usuario:Usuario {cpf: $cpf}) "
            "RETURN usuario as u"
        )
        result = self.query(query, cpf=cpf)
        return result[0]['u'] if result else None
    
    def get_vendedores(self):
        query = "MATCH (v:Vendedor) RETURN v"
        result = self.query(query)
        return [record["v"] for record in result]
    
    def get_vendedor_por_cnpj(self, cnpj):
        query = (
            "MATCH (v:Vendedor {cnpj: $cnpj}) "
            "RETURN v as v"
        )
        result = self.query(query, cnpj=cnpj)
        return result[0]['v'] if result else None
    
    def get_compras(self):
        query = """
            MATCH (u:Usuario)-[:REALIZA]->(c:Compra)-[co:CONTEM]->(p:Produto)
            RETURN u, c, p, co.quantidade AS quantidade
        """
        result = self.query(query)
        return result if result else None
    
    def get_compras_por_cpf(self, cpf):
        query = """
            MATCH (u:Usuario {cpf: $cpf})-[:REALIZA]->(c:Compra)-[co:CONTEM]->(p:Produto)
            RETURN u, c, p, co.quantidade AS quantidade
        """
        result = self.query(query, cpf=cpf)
        return result if result else None

    def get_favoritos(self):
        query = (
            "MATCH (u:Usuario)-[f:FAVORITOU]->(p:Produto) RETURN u as u, f as f, p as p"
        )
        result = self.query(query)
        return result if result else None
    
    def get_favoritos_por_cpf(self, cpf):
        query = (
            "MATCH (u:Usuario {cpf: $cpf})-[:FAVORITOU]->(p:Produto) RETURN u as u, p as p"
        )
        result = self.query(query, cpf=cpf)
        return result if result else None

    def adicionar_venda(self, idProduto, quantidade):
        query = (
            "MATCH (p:Produto {id: $idProduto}) "
            "SET p.estoque = p.estoque - $quantidade, "
            "p.vendas = coalesce(p.vendas, 0) + $quantidade "
            "RETURN p"
        )
        self.query(query, idProduto=idProduto, quantidade=quantidade)

    def get_node_count(self, label):
        query = f"MATCH (n:{label}) RETURN count(n) as count"
        result = self.query(query)
        return result[0]['count'] if result else 0
        
    def query(self, query, **kwargs):
        assert self._driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self._driver.session()
            response = list(session.run(query, **kwargs))
        except Exception as e:
            print("Query failed:", e)
        finally:
            if session is not None:
                session.close()
        return response

NEO4J_URI='neo4j+s://86e20313.databases.neo4j.io'
NEO4J_USERNAME='neo4j'
NEO4J_PASSWORD='hlPZgYIwS5OqmD2t8i7dc2FelFH131sxsj2IpynL4u4'

database = Neo4jConnection(NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD)
