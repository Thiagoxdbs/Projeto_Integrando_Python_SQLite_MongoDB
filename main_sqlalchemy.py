from matplotlib.pyplot import connect
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import inspect
from sqlalchemy import ForeignKey
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session



# Criando as tabelas com a herança da classe Base

Base = declarative_base()
engine = create_engine('sqlite:///memory')


class Cliente(Base):
    """
        Cria a tabela Cliente com o sqlalchemy
    """
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cpf = Column(String(9))
    endereco = relationship("Conta", back_populates="cliente")


class Conta(Base):
    """
        Cria a tabela endereço com o sqlalchemy
    """
    __tablename__ = "conta"
    id = Column(Integer, primary_key=True)
    tipo = Column(String, nullable=True)
    agencia = Column(String)
    num = Column(Integer, nullable=True)
    id_cliente = Column(Integer, ForeignKey("cliente.id"), nullable=False)

    cliente = relationship("Cliente", back_populates="endereco")


def cria_tabelas():
    """
        Cria as tabelas no sqlite
    """
    Base.metadata.create_all(engine)


# cria_tabelas()

# insp = inspect(engine)
# print(insp.get_table_names())

# Inserindo alguns dados

with Session(engine) as session:
    breno = Cliente(
        nome="Breno Campos",
        cpf="123456",
        endereco = [Conta(agencia='0001')]
    )
    simone = Cliente(
        nome="Simone Campos",
        cpf="654321",
        endereco=[Conta(agencia='0001')]
    )
    valdo = Cliente(
        nome="Valdo Campos",
        cpf="456123",
        endereco=[Conta(agencia='0001')]
    )

session.add_all([breno, simone, valdo])

session.commit()

# print(select(Cliente))
stmt = select(Cliente)

connection = engine.connect()
results = connection.execute(stmt).fetchall()

for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(Cliente)
results = connection.execute(stmt_count).fetchall()
for result in results:
    print(result)

stmt_where = select(Cliente).where(Conta.id.in_([2]))
results = connection.execute(stmt_where).fetchall()
for result in results:
    print(result)