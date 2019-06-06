from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker #gere novos objectos quando é gerada
from sqlalchemy.ext.declarative import declarative_base #para declarar como a base dados sera composta
from datetime import datetime #importar a data e tempo


conn = "sqlite:///dbservidor.sqlite"  # nome da base de dados
engine = create_engine(conn)
base = declarative_base()

class Artigo(base):
    __tablename__ = "Artigo" #nome da tabela

    id = Column(Integer, primary_key=True)  # id como inteiro e uma chave primaria, ou seja, a base de dados é que ira modificar o id automaticamente
    nome = Column(String(120))  #variavel em string
    marca = Column(String) #variavel em string
    preco = Column(Float) #variavel em float
    data_scrap = Column(DateTime, default=datetime.now)  # data do momento em que os artigos sao introduzidos
    imagem = Column(String)  # diretorio da imagem , variavel em string

    def __repr__(self):
        return '< Artigo: {} >'.format(self.id)

base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
