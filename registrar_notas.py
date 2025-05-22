def registrar_notas():
    notas = []

    print("Digite as notas dos alunos. Para encerrar, digite 'fim'.")
    while True:
        entrada = input("Nota: ")

        if entrada.lower() == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Digite um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"Média da turma: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")

# Executa o programa
if __name__ == "__main__":
    registrar_notas()
