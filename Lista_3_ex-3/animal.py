class Animal():
    def __init__(self,name,age,sound,species):
        self.__name = name
        self.__age = age
        self.__sound = sound
        self.__species= species

    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @property
    def sound(self):
        return self.__sound
    
    @property
    def species(self):
        return self.__species
    
    #setattr
    @name.setter
    def name(self,name):
        self.__name =name 

    @age.setter
    def age(self,age):
        self.__age=age

    @sound.setter
    def sound(self,sound):
        self.__sound = sound

    @species.setter
    def species(self,species):
        self.__species = species
    
    #metodos
    def exibir_informacao(self):
        print(f"Nome do animal:{self.name}")
        print(f"Idade do animal:{self.age}")        

    





