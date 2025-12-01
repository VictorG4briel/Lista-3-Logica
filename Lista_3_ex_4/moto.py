from Veiculo import Vehicle

class Motorcycle(Vehicle):
    def __init__(self,marca,modelo,ano):
        super().__init__(marca,modelo,ano)


    def mover(self):
        print("A moto está rodando em duas rodas")