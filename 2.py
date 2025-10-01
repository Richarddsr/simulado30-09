def classificar_imc(nome, imc):
    """
    Classifica o IMC de uma pessoa e retorna uma mensagem.
    
    Parâmetros:
    nome (str): Nome da pessoa
    imc (float): Valor do IMC
    
    Retorna:
    str: Mensagem com a classificação
    """
    if imc < 18.5:
        return f"{nome} está abaixo do peso."
    elif imc <= 24.9:
        return f"{nome} está com peso normal."
    elif imc <= 29.9:
        return f"{nome} está com sobrepeso."
    else:
        return f"{nome} está obeso."


# Programa principal
print("=== CLASSIFICADOR DE IMC ===")
print("Digite 'sair' no nome para encerrar o programa.\n")

while True:
    # Solicita o nome
    nome = input("Digite o nome: ").strip()
    
    # Verifica se o usuário quer sair
    if nome.lower() == "sair":
        print("\nPrograma encerrado. Até logo!")
        break
    
    # Solicita o IMC
    try:
        imc = float(input("Digite o IMC: "))
        
        # Chama a função e exibe o resultado
        resultado = classificar_imc(nome, imc)
        print(f"→ {resultado}\n")
        
    except ValueError:
        print("Erro: Por favor, digite um número válido para o IMC.\n")