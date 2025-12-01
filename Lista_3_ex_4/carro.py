from Veiculo import Vehicle

class Car(Vehicle):
    def __init__(self,marca,modelo,ano):
        super().__init__(marca,modelo,ano)


    def mover(self):
        print("O carro está rodando em quatro rodas")