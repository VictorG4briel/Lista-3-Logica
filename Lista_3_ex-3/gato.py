from animal import Animal

class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name,age,"Miado","Gato")
        
    def som(self):
        print("Miado")