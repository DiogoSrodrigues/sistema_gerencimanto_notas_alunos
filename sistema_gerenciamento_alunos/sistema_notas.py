import time
 
# 1. Variáveis iniciais
turma = []
 
print('🏫  --- Bem-vindo ao Sistema de Notas ---')
 
# 2. Laço principal que mantém o programa em execução
while True:
    print('''\n --- Menu Principal ---
          [1] - Cadastrar Aluno
          [2] - Ver Boletim
          [3] - Sair
          ''')
 
    opcao = input('➡️  Escolha uma opção: ')
 
    # Lógica para cadastrar um aluno
    if opcao == '1':
        nome = input('➡️  Nome do aluno: ')
 
        notas = []
        for i in range(3):
            while True:
                nota = float(input(f'➡️  Digite a nota {i + 1}: '))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break  # nota válida, sai do while
                else:
                    print('❌  Nota inválida. Digite um valor entre 0 e 10.')
    
        # Calcula a média das 3 notas
        media = (notas[0] + notas[1] + notas[2]) / 3
 
        # Determina a situação do aluno
        if media >= 7.0:
            situacao = 'Aprovado ✅'
        elif media >= 5.0:
            situacao = 'Recuperação ⚠️'
        else:
            situacao = 'Reprovado ❌'
 
        registro = f'{nome} | Notas: {notas[0]:.1f}, {notas[1]:.1f}, {notas[2]:.1f} | Média: {media:.2f} | {situacao}'
        turma.append(registro)  # adiciona o aluno à turma
        print('✅  Aluno cadastrado com sucesso.')
 
    # Lógica para ver o boletim
    elif opcao == '2':
        print('📋 --- Boletim da Turma ---')
        if not turma:  # verifica se a lista está vazia
            print('❌  Nenhum aluno cadastrado ainda.')
        else:
            for aluno in turma:
                print(aluno)
 
    # Lógica para sair
    elif opcao == '3':
        print('📤  Encerrando o sistema. Até logo!')
        time.sleep(2)  # pequena pausa
        break  # encerra o laço while
 
    # Lógica para opção inválida
    else:
        print('❌  Opção inválida. Por favor, escolha uma das opções do menu.')
