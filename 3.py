""" 3. Crie um programa para analisar salários de funcionários.
O programa deve ter uma função chamada analisar_salarios que receba uma lista com
os valores dos salários.
A função deve retornar:
a. O total de funcionários.
b. O maior salário.
c. O menor salário.
d. A quantidade de funcionários que ganham acima de R$ 3.000,00.
e. A média dos salários.
f. O programa deve:
g. Ler os salários até o usuário digitar -1.
h. Chamar a função e exibir os resultados. """

salarios = []
def analisar_salarios(salarios):
    total_funcionarios = len(salarios)
    maior_salario = max(salarios) if salarios else 0
    menor_salario = min(salarios) if salarios else 0
    acima_3000 = sum(1 for salario in salarios if salario > 3000)
    media_salarios = sum(salarios) / total_funcionarios if total_funcionarios > 0 else 0
    return total_funcionarios, maior_salario, menor_salario, acima_3000, media_salarios

if __name__ == "__main__":
    analisar_salarios()