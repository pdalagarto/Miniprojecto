from PyQt5.QtWidgets import QMessageBox, QFileDialog #libraria do PyQt5
import pandas as pd #é uma biblioteca para manipulação e análise de dados.
from app import db #importa a base de dados
from app.db import Artigo #importa a class Artigo da base de dados


def import_csv():
    file = QFileDialog()  # class que promove que os utilizadores permitam a selecao de ficheiros ou diretório
    file.setFileMode(QFileDialog.ExistingFile)  # o ficheiro tem de existir para ser selecionado

    if file.exec_():  # se a procura de ficheiros incia
        filenames = file.selectedFiles()[0] #diretorio do ficheiro selecionado
        con = db.conn #nome da base de dados
        ler = pd.read_csv(filenames) #le o documento csv contdio em filenames
        try:
            ler.to_sql(con=con, index_label='id', name=Artigo.__tablename__, if_exists='replace') #se o documento csv reunir as condicoes(nao pode conter id, tem de apresentar a,
            # tabela igual a apresentaçao da class Artigo) importa para a base de dados e substitui-a
        except ValueError: #se nao apresentar as condiçoes necessarias , apresenta uma mensagem de erro, e volta a "repetir"
            msg = QMessageBox()
            msg.setWindowTitle("Erro!")
            msg.setText("O seu ficheiro não está correcto!")
            msg.exec_()
            return

        msg = QMessageBox() #mensagem caso o documento csv seja bem importado
        msg.setWindowTitle("Verificação!")
        msg.setText("O seu ficheiro foi importado com sucesso!")
        msg.exec_()
