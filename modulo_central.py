# ============================================
# Sistema Acadêmico - Versão 1.1 (Interativa)
# Projeto: TecStart - Universidade Privada
# Módulo: Gestão Acadêmica (Simulado)
# ============================================

import time
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def pausa(segundos=1.5):
    time.sleep(segundos)

limpar_tela()
print("======================================")
print("   SISTEMA ACADÊMICO - TECSTART   ")
print("======================================")
pausa()

print("\n>>> Cadastro do Aluno\n")
pausa()

# Entrada de dados do aluno
nome = input("Digite o nome do aluno: ")
pausa()
matricula = input("Digite a matrícula: ")
pausa()
curso = input("Digite o curso: ")
pausa()
disciplina = input("Digite a disciplina: ")
pausa()

print("\n>>> Lançamento de Notas\n")
pausa()

nota1 = float(input("Digite a 1ª nota: "))
pausa()
nota2 = float(input("Digite a 2ª nota: "))
pausa()
nota3 = float(input("Digite a 3ª nota: "))
pausa()
frequencia = float(input("Digite a frequencia: "))
limpar_tela()
print("Processando dados do aluno...")
pausa(2)

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Exibição dos dados
print("======================================")
print("        DADOS DO ALUNO        ")
print("======================================")
pausa()

print(f"Nome: {nome}")
pausa()
print(f"Matrícula: {matricula}")
pausa()
print(f"Curso: {curso}")
pausa()

print("\n======================================")
print("      DADOS ACADÊMICOS      ")
print("======================================")
pausa()

print(f"Disciplina: {disciplina}")
pausa()
print(f"Nota 1: {nota1}")
pausa()
print(f"Nota 2: {nota2}")
pausa()
print(f"Frequência: {frequencia}%")
pausa()

print("\n======================================")
print("        RESULTADO FINAL        ")
print("======================================")
pausa()

print(f"Média Final: {media:.2f}")
pausa()

if media >= 7 and frequencia >= 75:
    print("Situação: APROVADO")
else:
    print("Situação: REPROVADO")

pausa()
print("\n======================================")
print("     FIM DO PROCESSAMENTO     ")
print("======================================\n")
