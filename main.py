import random


def main():
    lotofacil = list(range(1, 26))
    megasena = list(range(1, 61))
    quina = list(range(1, 81))

    numeros_selecionados = random.sample(lotofacil, 15)
    print("Números da Lotofácil:", sorted(numeros_selecionados))
    numeros_selecionados = random.sample(megasena, 6)
    print("Números da Mega-Sena:", sorted(numeros_selecionados))
    numeros_selecionados = random.sample(quina, 5)
    print("Números da Quina:", sorted(numeros_selecionados))

if __name__ == "__main__":
    main()
