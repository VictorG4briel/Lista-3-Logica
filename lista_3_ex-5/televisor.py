from abc import ABC, abstractclassmethod

class televisor(ABC):
    def __init__ (self,marca,modelo,tamanho):
        self.marca=marca
        self.modelo=modelo
        self.tamanho=tamanho
        
    @abstractclassmethod
    def ligar(self):
        pass

    @abstractclassmethod
    def desligar(self):
        pass

    @abstractclassmethod
    def numeroCanais(self):
        pass

    @abstractclassmethod
    def aumentarCanais(self):
        pass

    @abstractclassmethod
    def diminuirCanais(self):
        pass

    @abstractclassmethod
    def aumentarVolume(self):
        pass

    @abstractclassmethod
    def diminuirVolume(self):
        pass

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Tamanho: {self.tamanho} polegadas")

    
class Conectividade(ABC):

    @abstractclassmethod
    def conectar_internet(self):
        pass



    