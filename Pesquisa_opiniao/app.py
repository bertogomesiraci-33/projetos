"""
Atividade: Pesquisa de Satisfação - TudoWeb
Objetivo:Coletar e consolidar respostas de satisfação no atendimento.
Regra de negócio: 1- EXCELENTE, 2- BOM, 3- RUIM.
"""

import os
os.system("cls") # Limpa a tela no windows

# Inicialização dos contadores solicitados 
qtde_excelente = 0
qtde_bom = 0
qtde_ruim = 0

# Estrutura de repetição para coletar os dados dos entrevistados (de 1 até 50)
for i in range(1, 51):

    # Coleta dos dados do entrevistado
    print(f"\n--- Entrevistado {i} de 50 ---")
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))

    # Apresentação das opções e leitura da nota
    print("Opções de avaliação: 1 - EXCELENTE; 2 - BOM; 3 - RUIM")
    opiniao = int(input("informe sua nota (1, 2 ou 3): "))

    # Validação de dados de entrada com while
    while opiniao not in [1, 2, 3]:
        print("Opção inválida! Escolha apenas 1, 2 ou 3.") 
        opiniao = int(input("informe novamente sua nota (1, 2 ou 3): "))

    # Estruturas de decisão para totalizar as respostas
    if opiniao == 1:
        qtde_excelente += 1
    elif opiniao == 2:
        qtde_bom += 1
    elif opiniao == 3:
        qtde_ruim += 1

# Exibição dos resultados solicitados:
print("\n" + "=" * 40)
print("    RESULTADO DA PESQUISA")
print("=" * 40)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtde_excelente}")
print(f"b) Quantidade de respostas 'BOM': {qtde_bom}")
print(f"c) Quantidade de respostas 'RUIM': {qtde_ruim}")
print("=" * 40)

