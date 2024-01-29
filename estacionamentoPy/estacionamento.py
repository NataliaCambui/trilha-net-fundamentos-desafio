print("-----Estacionamento Cambui-----")

class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.preco_inicial = 3
        self.preco_por_hora = 2

    def adicionar_veiculo(self):
        placa = input("Digite a placa do veiculo para estacionar: ")
        self.veiculos.append(placa)
        print("Veiculo adicionado com sucesso.")

    def remover_veiculo(self):
        placa = input("Digite a placa do veiculo para remover: ")
        if placa in self.veiculos:
            horas = int(input("Digite a quantidade de horas que o veiculo permaneceu no estacionamento: "))
            valor_total = self.preco_inicial + (self.preco_por_hora * horas)
            self.veiculos.remove(placa)
            print(f"O veiculo {placa} foi removido e o preço total foi de: R$ {valor_total}")
        else:
            print("Desculpe, esse veículo não está estacionado aqui. Confira se digitou a placa corretamente.")

    def listar_veiculos(self):
        if self.veiculos:
            print(f"Os veiculos estacionados aqui são: {self.veiculos}")
        else:
            print("Não há veículos estacionados aqui.")

if __name__ == "__main__":
    estacionamento = Estacionamento()

    while True:
        opcao = int(input('''Escolha a opção que deseja realizar:
                            [1] Adicionar veiculo
                            [2] Remover veiculo
                            [3] Listar veiculos
                            [4] Finalizar\n'''))

        if opcao == 1:
            estacionamento.adicionar_veiculo()

        elif opcao == 2:
            estacionamento.remover_veiculo()
        elif opcao == 3:
            estacionamento.listar_veiculos()
        elif opcao == 4:
            print("Fim do programa. Volte sempre")
            break
        else:
            print("Opção inválida. Tente novamente.")

print(70*'-')