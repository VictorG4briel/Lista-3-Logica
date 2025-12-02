from televisor import televisor,Conectividade

class SmartTV(televisor,Conectividade):
    def __init__(self,marca,modelo,tamanho):
        super().__init__(marca,modelo,tamanho)
        self.volume=10
        self.canal=1

    def ligar(self):
        print("Ligando a Smart TV com sistema operacional Android TV...")

    def desligar(self):
        print("Desligando TV")

    def numeroCanais(self):
        return 100
    
    def aumentarCanais(self):
        if self.canal< self.numeroCanais():
            self.canal +=1
        print(f"Canal atual:{self.canal}")

    def diminuirCanais(self):
        if self.canal > 1:
            self.canal -= 1
        print(f"Canal atual:{self.canal}")

    def aumentarVolume(self):
        self.volume += 1
        print(f"Volume:{self.volume}")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        print(f"Volume:{self.volume}")

    def conectar_internet(self):
        print("Conectando via Wi-Fi")

    
