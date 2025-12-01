from animal import Animal
from cachorro import Dog
from gato import Cat

def registrar_animal():
    nome = input("Digite o nome do seu animal: ")
    idade = input("Digite a idade do seu animal: ")

    print("\nQual a especie do seu animal?")
    print("1- Cachorro")
    print("2-Gato")

    opcao = input("Escolha(1 ou 2):")
    if opcao == "1":
        animal = Dog(nome,idade)
    elif opcao == "2":
        animal = Cat(nome,idade)
    else:
        print("Opção invalida")
        return opcao
    
    return animal

def main():
    print("\n=== MENU PRINCIPAL ===")
    print("1 - Registrar Animal")
    print("2 - Sair")

    escolha = input("Escolha uma opção:")

    if escolha == "1":
        animal = registrar_animal()
        if animal:
            print("\n--- Dados do Animal ---")
            animal.exibir_informacao()
            print("\nSom do animal:")
            animal.som()

    elif escolha == "2":
        print("Saindo do programa...")
    else:
        print("Opção invalida")

if __name__ == "__main__":
    main()


