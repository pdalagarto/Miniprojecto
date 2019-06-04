from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QMessageBox, QFileDialog
import pandas as pd
from app.db import session, Artigo
from app import db

def import_csv():
    file = QFileDialog()  # class que promove que os utilizadores permitam a selecao de ficheiros ou diretório
    file.setFileMode(QFileDialog.ExistingFile)  # o ficheiro tem de existir para ser selecionado

    if file.exec_():  # se a procura de ficheiros incia
        filenames = file.selectedFiles()[0]
        con = db.conn
        df = pd.read_csv(filenames)
        try:
            df.to_sql(con=con, index_label='id', name=Artigo.__tablename__, if_exists='replace')
        except ValueError:
            msg = QMessageBox()
            msg.setWindowTitle("Erro!")
            msg.setText("O seu ficheiro não está correcto!")
            msg.exec_()
            return



        msg = QMessageBox()
        msg.setWindowTitle("Verificação!")
        msg.setText("O seu ficheiro foi importado com sucesso!")
        msg.exec_()
