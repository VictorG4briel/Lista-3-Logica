from account import Account

class ContaSalario(Account):
    def __init__(self, agency, agency_dig, code, account_number, account_dig, balance=0.0, employer=None):
        super().__init__(agency, agency_dig, code, balance)
        self.__account_number = account_number
        self.__account_dig = account_dig
        self.__employer = employer  

    # Getters
    @property
    def account_number(self):
        return self.__account_number

    @property
    def account_dig(self):
        return self.__account_dig

    @property
    def employer(self):
        return self.__employer

    # Setters
    @account_number.setter
    def account_number(self, account_number):
        self.__account_number = account_number

    @account_dig.setter
    def account_dig(self, account_dig):
        self.__account_dig = account_dig

    @employer.setter
    def employer(self, employer):
        self.__employer = employer

    def receive_salary(self, amount):
        if amount > 0:
            self.deposit(amount)
            print(f"Salário de R${amount:.2f} recebido da empresa {self.__employer}")

    def update_balance(self):
        print("Conta Salário: saldo não sofre atualização automática.")

    def __str__(self):
        return (
            f"{super().__str__()}\n"
            f"Conta Salário: {self.__account_number}-{self.__account_dig}\n"
            f"Empregador: {self.__employer}"
        )
