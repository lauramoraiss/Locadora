import os
from classes import *  


def cadastro():
    while True:
        os.system('cls')
        print("*╚═══❖•ೋ° 𝑪𝑨𝑫𝑨𝑺𝑻𝑹𝑶 °ೋ•❖═══╝*")
        print('')
        print("\n Selecione o que deseja cadastrar:")
        print("\n1 - Cliente \n2 - Filme \n3 - Jogo ")
        resp1 = int(input("\n -----> "))

        if resp1 == 1:
            print("•–––––– ᴠᴏᴄê ꜱᴇʟᴇᴄɪᴏɴᴏᴜ ᴄʟɪᴇɴᴛᴇ ––––––•")
            print('\n')
            nome = input("\nInsira seu nome: ")
            print('')
            idade = int("\nInsira sua idade: ")
            print('')
            cpf = int(input("\nInsira seu cpf: "))
            print('')
            cidade = input("\nInsira sua cidade: ")
            print('')
            estado = input("\nInsira seu estado: ")


        

        if resp1 == 2:
            print("•–––––– ᴠᴏᴄê ꜱᴇʟᴇᴄɪᴏɴᴏᴜ ꜰɪʟᴍᴇ ––––––•")
            print('\n')
            nome_filme = input("\nInsira o nome do filme: ")
            print('')
            genero_filme = input("\nInsira o gênero do filme: ")
            print('')
            duração = int(input("\nInsira o tempo de duração do filme(minutos): "))



        if resp1 == 3:
            print("•–––––– ᴠᴏᴄê ꜱᴇʟᴇᴄɪᴏɴᴏᴜ ᴊᴏɢᴏ ––––––•")
            print('\n')
            nome_jogo = input("\nInsira o nome do jogo: ")
            print('')
            plataforma = input("\nInsira a plataforma onde reside esse jogo: ")
            print('')
            faixa_etaria = input("\nInsira a faixa etária do jogo: ")

    


def listar():
    os.system('cls')
    print("*╚═══❖•ೋ° 𝑳𝑰𝑺𝑻𝑨𝑹 °ೋ•❖═══╝*")
    print('')
    print("\n Selecione o que deseja listar: ")
    print("\n1 - Clientes \n2 - Filmes \n3 - Jogos")
    resp2 = int(input("\n -----> "))

    
    if resp2 == 1:
        print("")






def registrar():
    os.system('cls')
    print("*╚═══❖•ೋ° 𝑹𝑬𝑮𝑰𝑺𝑻𝑹𝑨𝑹 °ೋ•❖═══╝*")








def alugar_devolver():
    os.system('cls')
    print("*╚═══❖•ೋ° 𝑳𝑰𝑺𝑻𝑨 𝑫𝑬 𝑰𝑻𝑬𝑵𝑺 𝑫𝑰𝑺𝑷𝑶𝑵Í𝑽𝑬𝑰𝑺 °ೋ•❖═══╝*")