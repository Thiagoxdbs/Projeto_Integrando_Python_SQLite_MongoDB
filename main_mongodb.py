import pymongo as pyM
from pprint import pprint

# Conectando ao MongoDB / Conecta ao cluster
client = pyM.MongoClient("mongodb connection string") # string retirada do mongodb atlas

# Buscando coleções
db = client.clientes # cria o db chaamado 'clientes'
collection = db.bank # cria a coleção chamada bank


# Inserindo dados na coleção bank
posts = [{
    "nome" : "Breno Campos",
    "cpf": "123456",
    "endereço": "Rua 26A, 132",
    "conta": "001",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Simone Alves",
    "cpf": "654321",
    "endereço": "Rua 25A, 101",
    "conta": "002",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Valdo Gonçalves",
    "cpf": "456123",
    "endereço": "Rua 32A, 58",
    "conta": "003",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}, {
    "nome" : "Thais Batista",
    "cpf": "321654",
    "endereço": "Rua 16A, 231",
    "conta": "004",
    "agencia": "0001",
    "tipo" : "corrente",
    "saldo": 0
}]

# postando = collection.insert_many(posts)

post = {
    "nome" : "Rodrigo Avelar",
    "cpf": "564231",
    "endereço": "Rua 58A, 92",
    "conta": "005",
    "agencia": "0002",
    "tipo" : "corrente",
    "saldo": 0
}
# postando = collection.insert_one(post)


# Recuperando dados da collection bank

pprint(collection.find())
find = collection.find()
for post in find:
    pprint(post)

print(collection.count_documents({}))

print(collection.count_documents({"agencia": "0001"}))

for post in collection.find({}).sort("nome"): # sort("campo a ser ordenado")
    pprint(post)


# Exclui a coleção bank
# db['bank'].drop()


