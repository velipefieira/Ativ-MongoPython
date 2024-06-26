import pymongo
import redis
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin:admin@tchongomongo.twf3usb.mongodb.net/?retryWrites=true&w=majority&appName=TchongoMongo"
mongoDatabase = pymongo.MongoClient(uri, server_api=ServerApi('1'))
try:
    mongoDatabase.admin.command('ping')
except Exception as e:
    print(e)

redisDatabase = redis.Redis(host= 'redis-17880.c256.us-east-1-2.ec2.redns.redis-cloud.com',
                   port= 17880,
                   password= '6iE3boUfKwTWBgKcR5LuLNI2D99IykDX')

global db
global comprasColecao
global produtosColecao
global usuariosColecao
global vendedoresColecao

db = mongoDatabase.MercadoLIvre
comprasColecao = db.Compras
produtosColecao = db.Produtos
usuariosColecao = db.Usuários
vendedoresColecao = db.Vendedores
