from Veiculo import Vehicle
from carro import Car
from moto import Motorcycle

def informacoes_veiculo():
    marca = input("Escreva a marca do seu veiculo:")
    modelo = input("Escreva o modelo do seu veiculo:")
    ano = input("Escreva o ano do seu veiculo:")

    print("Qual o tipo do seu veiculo?")
    print("1 - Carro")
    print("2 - Moto")

    escolha= input("Selecione (1 ou 2):")
    if escolha == "1":
        veiculo = Car(marca,modelo,ano)
    elif escolha == "2":
        veiculo = Motorcycle(marca,modelo,ano)
    else:
        print("Opção invalida")
        return escolha
    return veiculo

def main():
    info_veiculo = informacoes_veiculo()
    print("\nInformações do veiculo:")
    info_veiculo.exibir_informacao()
    print("\nForma de locomoção:")
    info_veiculo.mover()
    


if __name__ == "__main__":
    main()