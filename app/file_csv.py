from PyQt5.QtWidgets import QMessageBox, QFileDialog  # libraria do PyQt5
from app.db import session, Artigo  # importa a class Artigo da base de dados
import csv



def import_csv():
    file = QFileDialog()  # class que promove que os utilizadores permitam a selecao de ficheiros ou diretório
    file.setFileMode(QFileDialog.ExistingFile)  # o ficheiro tem de existir para ser selecionado

    if file.exec_():  # se a procura de ficheiros incia
        filename = file.selectedFiles()[0]  # diretorio do ficheiro selecionado
        with open(filename, 'r') as csvfile: #abre o ficheiro selecionado
            reader = csv.reader(csvfile) #guarda na variavel reader o ficheiro texto csv
            next(reader) #passa o cabeçalho
            for i in reader:
                artigo = Artigo(nome=i[0],marca=i[1],preco=float(i[2]),imagem=i[3]) #instacia artigo
                session.add(artigo)

            session.commit() #grava na base de dados


