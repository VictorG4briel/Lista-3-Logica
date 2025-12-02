from smartTY import SmartTV
from tvcomum import TVComum

def exibir_info():
    marca = input("Digite a marca da sua TV:")
    modelo = input("Digite o modelo da sua TV(smart ou comum):").lower()
    tamanho = int(input("Digite o tamanho da sua TV(Em polegadas):"))

    if (modelo == "smart"):
        TV = SmartTV(marca,modelo,tamanho)
    elif (modelo == "comum"):
        TV = TVComum(marca,modelo,tamanho)
    else:
        print("Insira um modelo valido:")
        return None
    
    input("Pressione qualquer tecla para ligar a TV...")
    TV.ligar()

    internet=input("Pressione * para se conectar a internet(ou -1 para ignorar):")
    if internet == "*":
        TV.conectar_internet()
    while True:
        aumentar=input("Pressione + para aumentar o volume ou - para diminuir:")
        if aumentar == "+":
            TV.aumentarVolume()
        elif aumentar == "-":
            TV.diminuirVolume()
        else:
            print("Opção invalida")
            return aumentar

        canal= input("Pressione > para aumnetar de canal ou < para diminuir:")
        if canal == ">":
            TV.aumentarCanais()
        elif canal == "<":
            TV.diminuirCanais()
        else:
            print("Opção invalida")
            return canal
        continuar = input("\nDeseja continuar? (S/N): ").upper()
        if continuar == "N":
            break
    return TV
    
def main():
    info_TV=exibir_info()
    if info_TV: 
        print("\n===== INFORMAÇÕES DA TV =====")
        print(f"Marca: {info_TV.marca}")
        print(f"Modelo: {info_TV.modelo}")
        print(f"Tamanho: {info_TV.tamanho} polegadas")
    

    
if __name__ == "__main__":
    main()