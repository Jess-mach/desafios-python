class Aviao:
    def __init__(self, modelo, empresa, origem, destino, num_passageiros, num_voo):
        self.modelo = modelo
        self.empresa = empresa
        self.origem = origem
        self.destino = destino
        self.num_passageiros = num_passageiros
        self.num_voo = num_voo

    def __str__(self):
        return (f"Modelo: {self.modelo}, Empresa: {self.empresa}, Origem: {self.origem}, "
                f"Destino: {self.destino}, Passageiros: {self.num_passageiros}, Número do Voo: {self.num_voo}")

class ControleDecolagem:
    def __init__(self):
        self.fila = []

    def adicionar_aviao(self, aviao):
        self.fila.append(aviao)
        print(f"Avião {aviao.num_voo} adicionado à fila.")

    def decolar_aviao(self):
        if self.fila:
            aviao = self.fila.pop(0)
            print(f"Avião {aviao.num_voo} está decolando.")
        else:
            print("Nenhum avião na fila para decolagem.")

    def total_aviões(self):
        return len(self.fila)

    def listar_aviões(self):
        if self.fila:
            print("Aviões na fila de decolagem:")
            for aviao in self.fila:
                print(aviao)
        else:
            print("Nenhum avião na fila de decolagem.")

    def proximo_a_decolar(self):
        if self.fila:
            print("Próximo a decolar:")
            print(self.fila[0])
        else:
            print("Nenhum avião na fila de decolagem.")

    def posicao_aviao(self, num_voo):
        for i, aviao in enumerate(self.fila):
            if aviao.num_voo == num_voo:
                print(f"Avião número {num_voo} está na posição {i + 1}.")
                return
        print(f"Avião número {num_voo} não encontrado na fila.")

# Exemplo de uso
controle = ControleDecolagem()

# Adicionando aviões à fila
aviao1 = Aviao("Boeing 737", "Avianca", "São Paulo", "Rio de Janeiro", 150, "AV123")
aviao2 = Aviao("Airbus A320", "Gol", "Rio de Janeiro", "Brasília", 180, "GOL456")
aviao3 = Aviao("Embraer 195", "Azul", "São Paulo", "Curitiba", 120, "AZ789")

controle.adicionar_aviao(aviao1)
controle.adicionar_aviao(aviao2)
controle.adicionar_aviao(aviao3)

# Operações com a fila
controle.total_aviões()
controle.listar_aviões()
controle.proximo_a_decolar()
controle.posicao_aviao("GOL456")
controle.decolar_aviao()
controle.listar_aviões()
controle.total_aviões()