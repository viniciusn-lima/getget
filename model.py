import peewee
import psycopg2
from peewee import PostgresqlDatabase
import json

pg_db = PostgresqlDatabase('postgres', user='getget@pg-hackaton', password='hackAX2345',host='pg-hackaton.postgres.database.azure.com', port=5432)

class BaseModel(peewee.Model):

    class Meta:
        database = pg_db
    
class Login(BaseModel):
    id_user = peewee.AutoField()
    nome_fantasia = peewee.CharField()
    cnpj = peewee.CharField()
    email = peewee.CharField()
    senha = peewee.CharField()

class Catalogo_Anuncio(BaseModel):
    id_anuncio = peewee.AutoField()
    foto  = peewee.CharField(null = True)
    servico  = peewee.CharField(null = True)
    responsavel  = peewee.CharField(null = True)
    descricao = peewee.CharField(null = True)
    preco  = peewee.CharField(null = True)
    tipo  = peewee.CharField(null = True)

def create_table_anuncio():
    Catalogo_Anuncio.create_table()
    print("Tabela 'Catalogo_Anuncio' criada com sucesso!")

def create_table_login():
    Login.create_table()
    print("Tabela 'Login' criada com sucesso!")

def insert_many_login(json_data):
    query = Login.insert_many(json_data)
    query.execute()
    return {'status':'inserted!'}

def insert_many_anuncio(json_data):
    query = Catalogo_Anuncio.insert_many(json_data)
    query.execute()
    return {'status':'inserted!'}

def select_many_anuncio():
    list_anuncio = []
    query = Catalogo_Anuncio.select().dicts()
    for row in query:
        list_anuncio.append(row)
        print(row)
    json_ = json.dumps(list_anuncio)
    return json_

def login(email,senha):
    email = Login.get(Logemailin.email==email)
    senha = Login.get(Login.senha==senha)
    if email ==1 and senha ==1:
        return {'status':'ok'}
    else:
        return {'status':'denied'}


