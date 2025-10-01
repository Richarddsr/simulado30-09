notas = []
alunos = []
acimaM = 0

for i in range(15):
    nota = float(input("Digite sua nota: "))
    aluno = input("Digite seu nome: ")
    alunos.append(aluno)
    if nota >= 0 and nota <= 10:
        notas.append(nota)
        if nota >= 6:
            acimaM += 1
    else:
        print("Nota inválida, digite uma nota entre 0 e 10.")

media = sum(notas) / len(alunos)
print("\n")
print(f"A média da turma é: {media}")
print(f"A maior nota é: {max(notas)}")
print(f"A menor nota é: {min(notas)}")
print(f"A quantidade de alunos com nota acima da média é: {acimaM}")