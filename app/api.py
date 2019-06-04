from app import db #da pasta app importa db, ou seja, base de dados


class Api():
    def add_artigo(self, nome, marca, preco, imagem):
        artigo = db.Artigo(nome=nome, marca=marca, preco=preco, imagem=imagem) #corresponde a variaveis em que os artigos se indentificam
        db.session.add(artigo) #adiciona o artigo na database
        db.session.commit() #salva a database

    def remove_artigo(self, id):
        artigo = db.session.query(db.Artigo).filter_by(id=id).first() #manda um query a base de dados para filtrar por id primeiro
        if artigo: #se tiver id, faz:
            db.session.delete(artigo) #elimina o artigo na database
            db.session.commit() #salva na database

    def modificar_artigo(self, id, novo_nome, novo_marca, novo_preco, novo_imagem):
        artigo = db.session.query(db.Artigo).filter_by(id=id).first() #manda um query a base de dados para filtrar por id primeiro
        if artigo: #se tiver id, faz:
            artigo.nome = novo_nome #substitui a variavel nome por novo_nome
            artigo.marca = novo_marca #substitui a variavel marca por novo_marca
            artigo.preco = novo_preco #substitui a variavel preço por novo_preço
            artigo.imagem = novo_imagem #substitui a variavel imagem por nova_imagem
            db.session.commit() #salva na database
