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
            cpf = int(input("\nInsira seu cpf: "))

            

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
        print("•–––––– ʟɪꜱᴛᴀ ᴅᴇ ᴄʟɪᴇɴᴛᴇꜱ ᴄᴀᴅᴀꜱᴛʀᴀᴅᴏꜱ ––––––•")
        print('\n')

        if len (Cliente) == 0:
            print("Nenhum cliente cadastrado encontrado")

        else:
            for chave, valor in Cliente.items():
                print(f"{chave}° - \t{valor.GetNome()}\n\t{valor.GetCpf()}\n\t{valor.GetAlugados()}")


    if resp2 == 2:
        print("•–––––– ʟɪꜱᴛᴀ ᴅᴇ ꜰɪʟᴍᴇꜱ ᴄᴀᴅᴀꜱᴛʀᴀᴅᴏꜱ ––––––•")
        print('\n')

        if len (Filme) == 0:
            print("Nenhum filme cadastrado encontrado")

        else:
            for chave, valor in Filme.items():
                print(f"{chave}° - \t{valor.Get}")



    if resp2 ==3:
        print("•–––––– ʟɪꜱᴛᴀ ᴅᴇ ᴊᴏɢᴏꜱ ᴄᴀᴅᴀꜱᴛʀᴀᴅᴏꜱ ––––––•")
        print('\n')

        if len (Jogo) == 0:
            print("Nenhum jogo cadastrado encontrado")

        else:
            for chave, valor in Jogo.items():
                print(f"{chave}° - \t{valor.Get}")




def registrar():
    os.system('cls')
    print("*╚═══❖•ೋ° 𝑹𝑬𝑮𝑰𝑺𝑻𝑹𝑨𝑹 °ೋ•❖═══╝*")
    print('')








def alugar_devolver():
    os.system('cls')
    print("*╚═══❖•ೋ° 𝑳𝑰𝑺𝑻𝑨 𝑫𝑬 𝑰𝑻𝑬𝑵𝑺 𝑫𝑰𝑺𝑷𝑶𝑵Í𝑽𝑬𝑰𝑺 °ೋ•❖═══╝*")
    print('')
    print("Selecione quais itens disponíveis deseja saber: ")
    print("\n1 - Filmes \n2 - Jogos")
    resp3 = int(input("\n -----> "))



    if resp3 == 1:
        print("•–––––– ʟɪꜱᴛᴀ ᴅᴇ ꜰɪʟᴍᴇꜱ ᴅɪꜱᴘᴏɴíᴠᴇɪꜱ ––––––•")
        print('\n')







    if resp3 == 2:
        print("•–––––– ʟɪꜱᴛᴀ ᴅᴇ ᴊᴏɢᴏꜱ ᴅɪꜱᴘᴏɴíᴠᴇɪꜱ ––––––•")
        print('\n')