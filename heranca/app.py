# Criando classe pai

class Ninja:
    def __init__(self, nacao, vila):
        self.nacao = nacao
        self.vila = vila
    
    def atacar(self):
        print("Jutsu bola de fogo")
    
    def esquiva(self):
        return ("Substituir")


# usando herança sem modificar nada
class Ambu(Ninja):
    pass

a2 = Ambu("Dale rato", "Fogo")


print(f"sem modificar: {a2.nacao} {a2.vila}")

# usando herança modificando algo

class Ambuu(Ninja):
    def __init__(self, nacao, vila, jutsu):
        super().__init__(nacao, vila)
        self.jutsu = jutsu

a1 = Ambuu("Montanha", "Folha", "Terra")

print(f"O ninja é de: {a1.nacao} e {a1.vila}. Jutsu de {a1.jutsu}")


# n1=Ninja("Fogo", "Folha")

# print(f"O ninja veio de {n1.nacao} e {n1.vila}")
# n1.atacar()
# print(f"{n1.esquiva()}")
# n1.esquiva()