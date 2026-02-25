class Carro:
    def __init__(self, cor, ano):
        self.cor = cor
        self.ano = ano

veiculo = Carro("Vermelho", "2026")
print(f"O veiculo tem a cor {veiculo.cor} e o ano {veiculo.ano}")

class Moto(Carro):
    pass

Novo_veiculo = Moto("Laranja", "2025")
print(f"A moto tem a cor {Novo_veiculo.cor} e o ano de {Novo_veiculo.ano}")