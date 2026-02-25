class Cpf:
    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def status(self):
        return f"{self.nome} e {self.numero}"
    

aluno = Cpf("Aluno1", 5015856)

print(f"{aluno.status()}")


class Gato:
    def __init__(self, nome, pelagem):
        self .nome = nome
        self .pelagem = pelagem
    
    def falar(self):
        return f"Miau"

    def comer(self):
        return f"Comeu ração"
    
    def dormir(self):
        return f"Dormiu"
    
meu_gato = Gato("Garfield", "Laranja")
              
print(f"Meu gato faz {meu_gato.falar()}")
print(f"Meu gato comeu? {meu_gato.comer()}")



class Veiculo:
    def __init__(self, modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

veiculo1=Veiculo("Civic","Vermelho",2015)
print(f"{veiculo1.modelo}")
print(f"{veiculo1.cor}")
print(f"{veiculo1.ano}")