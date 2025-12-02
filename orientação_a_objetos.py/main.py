# main.py

# Imports
from Cliente import Client
from account import Account
from Checking_Account import CheckingAccount
from Saving_Account import SavingsAccount
from contaSalario import ContaSalario

# Client Instance
client = Client(
    name="joão",
    cpf=12345678901,
    address="Rua das Amoras",
    address_number=16,
    address_complement= "Apartamento",
    dt_birth="12/02/1980",
    phone="55+ (48) 9 2837-2746",
    email="joao@gmail"
)

# CheckingAccount Instance
checkingAccount = CheckingAccount(
    agency=27346,
    agency_dig=3,
    code=456,
    account_number=152437,
    account_dig=9,
    balance=235.87
)

# SavingsAccount Instance
savingsAccount = SavingsAccount(
    agency=27346,
    agency_dig=3,
    code=456,
    account_number=27653,
    account_dig=5,
    balance=150.89
)
salary_account = ContaSalario(
    agency=27346,
    agency_dig=3,
    code=456,
    account_number=998877,
    account_dig=1,
    balance=0.0,
    employer="Empresa XYZ"
)

# Exibir informações
print("=== DADOS DO CLIENTE ===")
print(client)

print("\n=== CONTA CORRENTE ===")
print(checkingAccount)

print("\n=== CONTA POUPANÇA ===")
print(savingsAccount)

print("\n=== Receber salário na conta salário ===")
print(salary_account.receive_salary(3000.00))

print("\n=== ATUALIZANDO SALDOS ===")
checkingAccount.update_balance()
savingsAccount.update_balance()

# After the update
print("\n=== SALDOS APÓS ===")
print(checkingAccount)
print(savingsAccount)