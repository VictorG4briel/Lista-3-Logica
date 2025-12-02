class Account():
    #constructor
    def __init__(self,agency,agency_dig,code,balance=0.0):
        self.__agency = agency
        self.__agency_dig = agency_dig
        self.__code = code
        self.__balance = balance
    #Getters
    @property
    def agency(self):
        return self.__agency
    
    @property
    def agency_dig(self):
        return self.__agency_dig

    @property
    def code(self):
        return self.__code
    
    @property
    def balance(self):
        return self.__balance
    
    #settres
    @agency.setter
    def agency(self,agency):
        self.__agency = agency

    @agency_dig.setter
    def agency_dig(self,agency_dig):
        self.__agency_dig = agency_dig
    
    @code.setter
    def code(self,code):
        self.__code = code
    
    #Functions
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
    
    def __str__(self):
        return(
            f"Agencia:{self.__agency} - {self.agency_dig}\n"
            f"Codigo do banco:{self.__code}"
            f"Saldo: R${self.__balance:.2f}"
        )

    def update_balance(self):
        print(f"Valor atualizado:")
#Instancias
account = Account(4499 , 5 , 000)

#Exit


