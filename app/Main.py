from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem, QMessageBox, QFileDialog #limbraria necessaria do PyQt5 que está a ser utilizada pelo programa
from PyQt5.QtGui import QPixmap #limbraria utilizada para representação de imagem.
from ui.projecto4 import Ui_MainWindow  #importa tudo que esta em ui.projecto4.py
from ui.projecto4 import Ui_MainWindow2 #importa tudo que esta em ui.adicionar.py
from ui.projecto4 import Ui_MainWindow4 #importa tudo que esta em ui.modificar.py
from ui.projecto4 import Ui_MainWindow5 #importa tudo que esta em ui.pesquisar.py
from ui.projecto4 import Ui_MainWindow6 #importa tudo que esta em ui.mostrar_imagem.py
import csv #importa ficheiros em csv
from app.file_csv import import_csv #importa a class import_csv do file_csv.py
from app import db #importa a base de dados
from app.api import Api #importa a class Api de app.api


class Main():
    filter = None #inicia a variavel com o objecto vazio

    def __init__(self):
        self.g = Api()  # Vai buscar a class API do ficheiro api.py

        # Janela Principal
        self.main_window = QMainWindow()
        self.main_window_form = Ui_MainWindow()
        self.main_window_form.setupUi(self.main_window)
        self.main_window.show()

        # Janela Adicionar
        self.main_window2 = QMainWindow()
        self.main_window_form2 = Ui_MainWindow2()
        self.main_window_form2.setup(self.main_window2)

        # Janela Modificar
        self.main_window4 = QMainWindow()
        self.main_window_form4 = Ui_MainWindow4()
        self.main_window_form4.setup4(self.main_window4)

        # Janela Pesquisar
        self.main_window5 = QMainWindow()
        self.main_window_form5 = Ui_MainWindow5()
        self.main_window_form5.setup5(self.main_window5)

        # Janela Mostrar Imagem
        self.main_window6 = QMainWindow()
        self.main_window_form6 = Ui_MainWindow6()
        self.main_window_form6.setup6(self.main_window6)

        self.bindings() #chamar a funçao bindings a class , para que os butoes consigam "correr"
        self.database() #chamar a funcao database, para que mostra a base de dados no inicio

    def bindings(self): #Funçao onde se conectao todos os botoes
        self.main_window_form.add_pushButton_2.clicked.connect(self.show_jn2)  # mostra a janela "Adicionar"
        self.main_window_form2.guardar_pushButton.clicked.connect(
            self.guardar)  # quando carrega em guardar corre a funçao "def guardar"
        self.main_window_form2.cancelar_pushButton.clicked.connect(
            self.hide2)  # quando clica em cancelar corre a funcao "def hide2" que faz esconder a janela
        self.main_window_form.remove_pushButton_4.clicked.connect(
            self.remover)  # quando é clicado corre a funçao "def remover"
        self.main_window_form4.novo_cancelar_pushButton.clicked.connect(
            self.hide4)  # quando clica em cancelar corre a funcao "def hide4" que faz esconder a janela
        self.main_window_form.modify_pushButton_3.clicked.connect(
            self.show_jn4)  # mostra a janela da funçao "def show_jn4", quando carregamos em modificar
        self.main_window_form4.novo_guardar_pushButton.clicked.connect(
            self.modificar)  # quando carregamos em modificar corre a funçao "def modificar"
        self.main_window_form2.imagem_pushButton.clicked.connect(self.explorer)
        self.main_window_form4.novo_imagem_pushButton.clicked.connect(self.explorer)
        self.main_window_form.search_pushButton.clicked.connect(self.show_jn5)
        self.main_window_form5.cancelar_pushButton.clicked.connect(self.hide5)
        self.main_window_form6.sair_pushbutton.clicked.connect(self.hide6)
        self.main_window_form.treeWidget.doubleClicked.connect(self.show_jn6)
        self.main_window_form5.pesquisar_pushButton.clicked.connect(self.button_pesquisar)
        self.main_window_form.reset_pushButton.clicked.connect(self.clear_database) #quando se clicla no botao reset conecta-se a funçao "def clear_database"
        self.main_window_form5.preco_checkBox.clicked.connect(self.ativa_precos)
        self.main_window_form5.data_checkBox.clicked.connect(self.ativa_data)
        self.main_window_form.exportar_pushButton.clicked.connect(self.extrair_csv)
        self.main_window_form.importar_pushButton.clicked.connect(import_csv)

    def guardar(self):
        inp = self.main_window_form2.preco_lineEdit.text()  # guarda o input de preço em inp
        try:
            preco = float(inp)  # verifica se preço é um float
        except ValueError:  # Se nao for, aparece uma janela de "Erro!", e repete o processo
            msg = QMessageBox()
            msg.setWindowTitle("Erro!")
            msg.setText("O valor é invalido!")
            msg.exec_()
            return

        if self.main_window_form2.nome_lineEdit.text() == "": #se o nome estiver em branco, mostra uma mensagem, e repete o processo
            msg = QMessageBox()
            msg.setWindowTitle("Erro!")
            msg.setText("Tem de introduzir um Nome")
            msg.exec_()
            return
        if self.main_window_form2.marca_lineEdit.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Erro!")
            msg.setText("Tem de introduzir uma Marca")
            msg.exec_()
            return
        if self.main_window_form2.imagem_lineEdit.text() == "":
            msg = QMessageBox()
            msg.setWindowTitle("Erro!")
            msg.setText("Tem de introduzir uma Imagem!")
            msg.exec_()
            return

        self.g.add_artigo(nome=self.main_window_form2.nome_lineEdit.text(),
                          marca=self.main_window_form2.marca_lineEdit.text(),
                          preco=preco,
                          imagem=self.main_window_form2.imagem_lineEdit.text())  # funçao que corre na "api.py" "def add_artigo"
        self.hide2()
        self.main_window_form.treeWidget.clear() #limpa a demostraçao da base de dados na treewidget
        self.database() #insera de novo com as alteraçoes feitas pelo utilizador

    def remover(self):
        get_Selected = self.main_window_form.treeWidget.selectedItems()  # seleção do artigo que o utilizador pretende
        if get_Selected:  # se selecionada
            remove = get_Selected[0].text(0)  # vai buscar o artigo selecionado
            self.g.remove_artigo(remove)  # remove o artigo

        self.main_window_form.treeWidget.clear()  # limpa a janela(treewidget) que mostra a database
        self.database()  # mostra a database, com as alteraçoes feitas na janela(treewidget)

    def modificar(self):
        inp = self.main_window_form4.novo_preco_lineEdit.text()
        try: #utilizador tenta introduzir um float, caso de erro aparece a menssagem "O valor é invalido"
            preco = float(inp)
        except ValueError:
            msg = QMessageBox() #Introduz na variavel msg a janela de texto(widget do pyqt5)
            msg.setWindowTitle("Erro!") #Titulo da janela de texto
            msg.setText("O valor é invalido!") #Introduz a Menssagem que queremos
            msg.exec_() #executa
            return #volta a repetir o processo sem parar o programa

        get_modificar = self.main_window_form.treeWidget.selectedItems()  # seleção do artigo que o utilizador pretende
        if get_modificar: #se o artigo for selecionado
            artigo_selecionado = get_modificar[0].text(0) #artigo selecionado com o texto que a seleçao se identifica
            if self.main_window_form4.novo_nome_lineEdit.text() == "": #na janela modificar, se a linha onde se introduz o nome estiver em branco
                msg = QMessageBox() #Introduz na variavel msg a janela de texto(widget do pyqt5)
                msg.setWindowTitle("Erro!")#Titulo da janela de texto
                msg.setText("Introduza um Nome")#Introduz a Menssagem que queremos
                msg.exec_()  #executa
                return #volta a repetir o processo sem parar o programa
            if self.main_window_form4.novo_marca_lineEdit.text() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Erro!")
                msg.setText("Introduza uma Marca")
                msg.exec_()
                return
            if self.main_window_form4.novo_imagem_lineEdit.text() == "":
                msg = QMessageBox()
                msg.setWindowTitle("Erro!")
                msg.setText("Introduza uma Imagem")
                msg.exec_()
                return

            self.g.modificar_artigo(artigo_selecionado, novo_nome=self.main_window_form4.novo_nome_lineEdit.text(),
                                    novo_marca=self.main_window_form4.novo_marca_lineEdit.text(),
                                    novo_preco=preco,
                                    novo_imagem=self.main_window_form4.novo_imagem_lineEdit.text())
            #inicia a funçao que esta na api.Api() def modificar_artigo, em que, o artigo selecionado

        self.hide4() #inicia a def hide4, que faz esconder a janela de modificar
        self.main_window_form.treeWidget.clear() #limpa a janela de apresentação
        self.database() #introduz a funçao def database, para introduzir de novo a base de dados com as alterações

    def explorer(self):
        file = QFileDialog() #class que promove que os utilizadores permitam a selecao de ficheiros ou diretório
        file.setFileMode(QFileDialog.ExistingFile) #o ficheiro tem de existir

        if file.exec_(): # se a procura de ficheiros incia
            filenames = file.selectedFiles() #os ficheiros selecionados(o diretorio), terao como variavel "filenames"

            self.main_window_form2.imagem_lineEdit.setText(filenames[0]) #para a linha de ediçao da janela
            # main_windows_form2(janela de adicionar), com o nome imagem_lineedit, insere o texto da variavel
            # "filenames[0]"(ficheiros selecionados)
            self.main_window_form4.novo_imagem_lineEdit.setText(filenames[0]) #repete-se a mesma coisa para a janela Modificar

    def pesquisar(self):
        self.main_window_form5.min_doubleSpinBox.setDisabled(True) #Desativar o preco minimo
        self.main_window_form5.max_doubleSpinBox.setDisabled(True) #Desativar o preço maximo
        self.main_window_form5.min_dateTimeEdit.setDisabled(True) #Desativar a data minima
        self.main_window_form5.max_dateTimeEdit.setDisabled(True) #Desativar a data maxima

        nome = db.session.query(db.Artigo.nome).all() #vai buscar todos os artigos.nome da base de dados e introduz na variavel nome
        self.main_window_form5.nome_comboBox.clear() #apaga tudo o que tiver na combobox da janela pesquisar
        self.main_window_form5.nome_comboBox.addItem("") #adiciona um item em branco, para que seja possivel pesquisar uma marca ou preço, sem introduzir um nome
        lista_nome = [] #cria uma lista
        for i in nome: #para a variavel i em nome faz:
            if i not in lista_nome: #se i nao está na lista_nome
                lista_nome.append(i) #adiciona i à lista_nome, ou seja, i esta dentro da variavel nome
                self.main_window_form5.nome_comboBox.addItem(i[0]) #adiciona i a combobox Nome:
        self.main_window_form5.nome_comboBox.setCurrentText(None) #para combobox nome na janela pesquisar, para o valor inicial nao ira ter nenhum objecto atribuido
        #Isto é para a combobox do nome e marca, apaga tudo, adiciona uma string em branco, verifica se os objectos da lista
        #sao repetidos, se nao forem adiciona, se forem nem se quer aparecem, e o ojecto inical é nenhum(None)

        marca = db.session.query(db.Artigo.marca).all()
        self.main_window_form5.marca_comboBox.clear()
        self.main_window_form5.marca_comboBox.addItem("")
        lista_marca = []
        for i in marca:
            if i not in lista_marca:
                lista_marca.append(i)
                self.main_window_form5.marca_comboBox.addItem(i[0])
        self.main_window_form5.marca_comboBox.setCurrentText(None)
        #É a mesma coisa que o nome, mas agora para a marca

    def ativa_precos(self):
        if self.main_window_form5.preco_checkBox.isChecked(): #se a checkbox estiver com o visto
            self.main_window_form5.min_doubleSpinBox.setEnabled(True) #ativa a min_doublespinbox
            self.main_window_form5.max_doubleSpinBox.setEnabled(True) #ativa a max_doublespinbox
        else: #se nao estiver com o visto
            self.main_window_form5.min_doubleSpinBox.setEnabled(False) #desativa
            self.main_window_form5.max_doubleSpinBox.setEnabled(False)

    def ativa_data(self): #é igual a função do ativa_precos so que para a data
        if self.main_window_form5.data_checkBox.isChecked():
            self.main_window_form5.min_dateTimeEdit.setEnabled(True)
            self.main_window_form5.max_dateTimeEdit.setEnabled(True)
        else:
            self.main_window_form5.min_dateTimeEdit.setEnabled(False)
            self.main_window_form5.max_dateTimeEdit.setEnabled(False)

    def button_pesquisar(self):
        nome = self.main_window_form5.nome_comboBox.currentText()  # retira o valor contido no nome da janela pesquisar
        marca = self.main_window_form5.marca_comboBox.currentText() # retira o valor contido na marca da janela pesquisar

        if self.main_window_form5.preco_checkBox.isChecked(): #se a checkbox tiver o visto
            preco_min = self.main_window_form5.min_doubleSpinBox.value() #retira o valor que esta inserido e mete-o na variavel preco_min
            preco_max = self.main_window_form5.max_doubleSpinBox.value() #retira o valor que esta inserido e mete-o na variavel preco_max
        else: #se nao tiver o visto
            preco_min = None #preco_min é igual a None
            preco_max = None #preco_max é igual a None

        #repete-se para a data
        if self.main_window_form5.data_checkBox.isChecked():
            data_min = self.main_window_form5.min_dateTimeEdit.date() #Imprime a data "PyQt5.QtCore.QDate(2019, 05, 20)"
            datascrap_min = data_min.toPyDate() #Imprime 2019-05-20

            data_max = self.main_window_form5.max_dateTimeEdit.date() #Imprime a data "PyQt5.QtCore.QDate(2019, 05, 20)"
            datascrap_max = data_max.toPyDate() #Imprime 2019-05-20

        else:
            datascrap_min = None
            datascrap_max = None

        self.filter = {
            "nome": nome,
            "marca": marca,
            "preco": [preco_min, preco_max],
            "datascrap": [datascrap_min, datascrap_max]
        }
        self.hide5() #esconde a janela de pesquisa
        self.database() #insere a base de dados

    def database(self):
        if self.filter is not None: #se houver filtro
            artigo = db.session.query(db.Artigo) #manda um query a base de dados
            if self.filter["nome"]: #se filtro for no nome
                query = db.session.query(db.Artigo).filter_by(nome=self.filter["nome"]) #manda um query a base de dados para filtrar por nome
                artigo = artigo.intersect(query) #tudo o que estiver na base de dados é interceptado com o query do nome
            if self.filter["marca"]:
                query = db.session.query(db.Artigo).filter_by(marca=self.filter["marca"])
                artigo = artigo.intersect(query)
            if self.filter["preco"][0] is not None or self.filter["preco"][1] is not None:
                query = db.session.query(db.Artigo).filter(db.Artigo.preco >= self.filter["preco"][0])\
                    .filter(db.Artigo.preco <= self.filter["preco"][1]) #recolhe todos os valor que estao entre o preço minimo e o preço maximo
                artigo = artigo.intersect(query) #interceção dos artigos
            if self.filter["datascrap"][0] is not None or self.filter["datascrap"][1] is not None:
                query = db.session.query(db.Artigo).filter(db.Artigo.data_scrap >= self.filter["datascrap"][0])\
                    .filter(db.Artigo.data_scrap <= self.filter["datascrap"][1])  # recolhe todas as datas, entre as datas escolhidas
                artigo = artigo.intersect(query)

        else: #se nao tiver filtros
            artigo = db.session.query(db.Artigo).all() #manda um pedido a base de dados para recolher todos os artigos que se encontram na db.Artigo

        self.main_window_form.treeWidget.clear() #limpa a janela que mostra a base de dados

        for i in artigo: #para i em artigos
            item = QTreeWidgetItem([
                str(i.id),
                i.nome,
                i.marca,
                str(i.preco),
                str(i.data_scrap).split(" ")[0],
                str(i.imagem)
            ])
            self.main_window_form.treeWidget.addTopLevelItem(item) #adiciona a janela de demostração os items recolhidos em artigos

    def clear_database(self): #limpa a janela de visualizaçao da database e insere-a de novo
        artigo = db.session.query(db.Artigo).all()
        self.main_window_form.treeWidget.clear()

        for i in artigo:
            item = QTreeWidgetItem([
                str(i.id),
                i.nome,
                i.marca,
                str(i.preco),
                str(i.data_scrap).split(" ")[0],
                str(i.imagem)
            ])
            self.main_window_form.treeWidget.addTopLevelItem(item)

    def extrair_csv(self):
        if self.filter is not None:
            artigo = db.session.query(db.Artigo)  # manda um query a base de dados
            if self.filter["nome"]:  # se filtro for no nome
                query = db.session.query(db.Artigo).filter_by(nome=self.filter["nome"])  # manda um query a base de dados para filtrar por nome
                artigo = artigo.intersect(query)  # tudo o que estiver na base de dados é interceptado com o query do nome
            if self.filter["marca"]:
                query = db.session.query(db.Artigo).filter_by(marca=self.filter["marca"])
                artigo = artigo.intersect(query)
            if self.filter["preco"][0] is not None or self.filter["preco"][1] is not None:
                query = db.session.query(db.Artigo).filter(db.Artigo.preco >= self.filter["preco"][0]) \
                    .filter(db.Artigo.preco <= self.filter["preco"][1])  # recolhe todos os valor que estao entre o preço minimo e o preço maximo
                artigo = artigo.intersect(query)  # interceção dos artigos
            if self.filter["datascrap"][0] is not None or self.filter["datascrap"][1] is not None:
                query = db.session.query(db.Artigo).filter(db.Artigo.data_scrap >= self.filter["datascrap"][0]) \
                    .filter(db.Artigo.data_scrap <= self.filter["datascrap"][1])  # recolhe todas as datas, entre as datas escolhidas
                artigo = artigo.intersect(query)

        else:  # se nao tiver filtros
            artigo = db.session.query(db.Artigo).all()


        file = './Ficheiros/export.csv'

        with open(file, 'w') as csvfile:
            outcsv = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            cabecalho = db.Artigo.__table__.columns.keys()

            outcsv.writerow(cabecalho)

            for gravar in artigo:
                outcsv.writerow([getattr(gravar, c) for c in cabecalho])

        msg = QMessageBox()
        msg.setWindowTitle("Verificação!")
        msg.setText("O seu ficheiro foi exportado")
        msg.exec_()

    def show_jn2(self):
        self.main_window2.show()  # mostra a janela

    def show_jn4(self):
        self.main_window4.show()  # mostra a janela

    def show_jn5(self):
        self.main_window5.show()  # mostra a janela do pesquisar
        self.pesquisar()

    def show_jn6(self):
        get_Selected = self.main_window_form.treeWidget.selectedItems()  # seleção do artigo que o utilizador pretende
        if get_Selected:  # se selecionada
            id = get_Selected[0].text(0)  # regista id da seleçao e guarda na variavel id
            artigo = db.session.query(db.Artigo).filter_by(id=id).first()  #

            self.main_window_form6.id_lineEdit.setText(str(artigo.id))  # apresenta o id do artigo selecionado é convertido em str
            # para visualizar, porque verdadeiramente o id é um inteiro como se pode ver na pasta api.py
            self.main_window_form6.nome_lineEdit.setText(artigo.nome)  # apresenta o nome do artigo selecionado
            self.main_window_form6.marca_lineEdit.setText(artigo.marca)  # apresenta a marca do artigo selecionado
            self.main_window_form6.preco_lineEdit.setText(str(artigo.preco))
            self.main_window_form6.datascrap_lineEdit.setText(str(artigo.data_scrap))
            self.main_window_form6.imagem_lineEdit.setText(str(artigo.imagem))

            pixmap = QPixmap(artigo.imagem)  # "converte" o directorio, para a variavel pixmap
            pixmap = pixmap.scaled(400, 400) #redimensiona a foto para 400*400 que é o tamanho da "label"
            self.main_window_form6.imagem_label.setPixmap(pixmap)  # apresenta a imagem na label(widget utilizado no qtdesigner)

        self.main_window6.show() #mostra a janela do artigo selecionado

    def hide2(self):
        self.main_window2.hide()  # esconde a janela

    def hide4(self):
        self.main_window4.hide()  # esconde a janela

    def hide5(self):
        self.main_window5.hide()

    def hide6(self):
        self.main_window6.hide()
