class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.__nome = nome
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def dar_like(self):
        self.__likes += 1

    @property
    def nome(self, value):
        return self.__nome = value.title()
    

class Serie:

    def __init__(self, nome, ano, temporada):
        self.__nome = nome
        self.__ano = ano
        self.__temporada = temporada