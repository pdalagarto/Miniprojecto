from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os

conn = "sqlite:///dbservidor.sqlite"  # nome da base de dados
engine = create_engine(conn)
base = declarative_base()

class Artigo(base):
    __tablename__ = "Artigo"

    id = Column(Integer, primary_key=True)  # id como inteiro
    nome = Column(String(120))  # nome como uma string
    marca = Column(String)
    preco = Column(Float)
    data_scrap = Column(DateTime, default=datetime.now)  # data do momento em que os artigos forem introduzidos
    imagem = Column(String)  # diretorio

    def __repr__(self):
        return '< Artigo: {} >'.format(self.id)

base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
