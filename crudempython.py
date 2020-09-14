# -*- coding: utf-8 -*-
"""CRUDemPython.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16O10qOdsXRPHamKx-i7xVNSLpoUWzXR2
"""

#ETE PORTO DIGITAL
#AD - CRUD em Python
#PROFESSOR CLOVES ROCHA
class Estudante:

    def __init__(self, nome, senha):  # Assim, você pode facilmente criar um estudante
        self.nome = nome
        self.senha = senha

    def alterar_senha(self, senha_antiga, senha_nova):
        if self.senha == senha_antiga:
            self.senha = senha_nova
            return True  # Sucesso
        else:
            return False  # Senha atual não confere

class Interface:

    estudantes = []

    def cadastrar_estudante(self):
        nome = input('Qual é o nome do estudante?\n')
        senha = input('Qual é a senha desejada?\n')

        self.estudante.append(estudante(nome, senha))
        print('Estudante adicionado!')

    def listar_estudantes(self):
        for i, estudante in enumerate(self.estudantes):
            print(i, estudante.nome)

    def alterar_senha(self):
        numero_estudante = input('Qual é o número de listagem do estudante?')
        numero_estudante = int(numero_estudante)

        senha_antiga = input('Qual é a senha atual?\n')
        senha_nova = input('Qual é a senha nova desejada?\n')
        sucesso = self.estudante[numero_estudante].alterar_senha(senha_antiga, senha_nova)

        if sucesso:
            print('Alteração realizada!')
        else:
            print('Erro ao tentar alterar senha!')

    def loop(self):
        while True:
            ad = input('\n1 - Listar estudantes\n2 - Cadastrar estudante\n3 - Alterar senha\n')
            if ad == '1':
                self.listar_estudantes()
            elif ad == '2':
                self.cadastrar_estudante()
            elif ad == '3':
                self.alterar_senha()
            else:
                print('Não entendi!')
                continue


if __name__ == '__main__':
    interface = Interface()
    interface.loop()