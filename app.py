from classes import *
from func import *

while True:
    def ls():
        os.system('pause')
        os.system('cls')
            
    def menu():
        print("\nSeja bem-vindo a locadora CineMania\n")
        print("Selecione uma opção:")
        print("\n 1- Cadastrar \n 2- Listar \n 3- Registrar \n 4- Alugar e Devolver\n 0- Sair ")
        escolha = int(input("\n ------> "))


        match escolha:
            case 1:
                cadastro()
            case 2:
                listar()
            case 3:
                registrar()
            case 4:
                alugar_devolver()
            case 0:
                print("Saindo...")
                os.system("pause")
            case _:
                print("Escolha Inválida!")
                os.system("pause")




