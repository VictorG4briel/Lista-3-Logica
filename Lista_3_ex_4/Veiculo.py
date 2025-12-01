class Vehicle():
    def __init__(self,marca,modelo,ano):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    @property
    def marca(self):
        return self.__marca
    
    @property
    def modelo(self):
        return self.__modelo
    
    @property
    def ano(self):
        return self.__ano
    
    @marca.setter
    def marca(self,marca):
        self.__marca = marca 

    @modelo.setter
    def modelo(self,modelo):
        self.__modelo = modelo
    
    @ano.setter
    def ano(self,ano):
        self.__ano = ano


    def exibir_informacao(self):
        print(f"Marca do veiculo:{self.marca}")
        print(f"Modelo do veiculo:{self.modelo}")
        print(f"Ano do veiculo:{self.ano}")
        

