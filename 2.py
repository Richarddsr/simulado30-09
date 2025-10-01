nomes = []
pesos = []

def classificarIMC():
    while True:
        peso = float(input("Digite seu peso em kg:"))
        pesos.append(peso)
        nome = input("Digite seu nome:")
        nomes.append(nome)
        if peso <= 18.5:
            print(f"{nome}, você está abaixo do peso.")
        elif peso > 18.5 and peso <= 24.9:
            print(f"{nome}, você está com o peso ideal.")
        elif peso > 24.9 and peso <= 29.9:
            print(f"{nome}, você está com sobrepeso.")
        elif peso > 29.9 and peso <= 34.9:
            print(f"{nome}, você está com obesidade grau I.")
        sair = input("Deseja sair? (s/n)")
        if sair.lower() == 's':
            break
        print(f"a classificação de IMC foi feita para {len(nomes)} pessoas.")
        nomes = sorted(nomes, reverse=True)
        

















if __name__ == "__main__":
    classificarIMC()