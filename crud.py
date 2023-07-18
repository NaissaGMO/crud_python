arq = open("CrudAlunos.txt")

print('1- Inserir aluno \n2- Excluir aluno \n3- Editar informações do aluno \n4- Listas alunos')
menu = int(input("Digite o número que corresponde a ação desejada: "))

if menu == 1:
    print("Inserir aluno")
    arq = open("CrudAlunos.txt", "a")
    NomeAluno = str(input("Digite o nome do aluno: "))
    MatriculaAluno = int(input("Digite a matrícula do aluno: "))
    convercao = str(MatriculaAluno)
    arq.write("\n" + NomeAluno + ", " + convercao)
    arq.close()

elif menu == 2:
    print("Remover Aluno - coloque as mesmas informações fornecidas no cadastro do aluno")
    Matricula = input("Digite a matrícula do aluno: ")

    with open("CrudAlunos.txt", "r") as arquivo:
        linhas = arquivo.readlines()
    numero_linha = None
    for index, linha in enumerate(linhas):
        if Matricula in linha:
            numero_linha = index
            break

    if numero_linha is not None:
        with open("CrudAlunos.txt", "w") as arquivo:
            for index, linha in enumerate(linhas):
                if index != numero_linha:
                    arquivo.write(linha)
    else:
        print(f"Matrícula '{Matricula}' não encontrada.")
    
elif menu == 3:
    print("Editar informações do aluno")
    matricula = input("Digite a matrícula do aluno -coloque os mesmos números usados no cadastro do aluno- ")
    NomeAluno = str(input("Edite o nome do aluno: "))
    MatriculaAluno = input("Edite a matrícula do aluno: ")
    novo_valor = NomeAluno + ", " + MatriculaAluno

    with open("CrudAlunos.txt", "r") as arquivo_leitura:
        linhas = arquivo_leitura.readlines()

    numero_linha = None
    for i, linha in enumerate(linhas):
        if matricula in linha:
            numero_linha = i
            break

    if numero_linha is not None:
        with open("CrudAlunos.txt", "w") as arquivo_escrita:
            for i, linha in enumerate(linhas):
                if i == numero_linha:
                    arquivo_escrita.write(novo_valor + "\n")
                else:
                    arquivo_escrita.write(linha)
    else:
        print(f"Matrícula '{matricula}' não encontrada.")


elif menu == 4:
    ler = open("CrudAlunos.txt", "r")
    print(ler.read())
    ler.close()
else:
    print('Opção inválida')
