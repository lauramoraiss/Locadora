
class Item:
    def __init__ (self, código: int, título: str):
        self.__codigo = código
        self.__titulo = título
        self.__disponibiliade = True 


    def Pegar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False
            



    def Largar(self):
        if self.disponivel:
            self.disponivel = True
            return True
        return False




class Filme(Item):
    def __init__(self, código: int, título: str, gênero: str, duração: int):
        Item.__init__(self, código, título)
        self.__genero = gênero
        self.__duracao = duração




class Jogo(Item):
    def __init__(self, código: int, título: str, plataforma: str, faixa_etária: int):
        Item.__init__(self, código, título)
        self.__plataforma = plataforma
        self.__faixaetaria = faixa_etária




class Cliente: #A classe Cliente deve ser capaz de locar e devolver itens
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__alugados = []


    def alugar(self, item:Item):
        if item.alugar():
            self.itensAlugados.append(item)
            return True
        return False
    
    def devolução(self, item:Item):
        if item.devol():
            self.itensAlugados.append(item)
            return True
        return False
    

    def listaritens(self):
        return [Item.titulo for item in self.itens.Alugados]




class Locadora: 
    def __int__(self):
        self.__clientes = []
        self.__itens = []


    def CadastrarClientes(self, cliente:Cliente):
        self.clientes.append(cliente)
        print(f'Cliente {cliente.nome} foi cadastrado com sucesso!')


    def CadastrarItens(self, item:Item):
        self.itens.append(item)
        print(f'Item {item.nome} foi cadastrado com sucesso!')



    def ListarClientes(self):
        print("•–––––– ᴄʟɪᴇɴᴛᴇꜱ ᴄᴀᴅᴀꜱᴛʀᴀᴅᴏꜱ ––––––•")
        if len(self.clientes) > 0:
            for cliente in self.clientes:
                print(f'- {cliente.nome} | (CPF: {cliente.cpf})')
            else:
                print("Nenhum cliente cadastrado")

        

    def ListarItens(self):
        print("•–––––– ɪᴛᴇɴꜱ ᴅᴀ ʟᴏᴄᴀᴅᴏʀᴀ ––––––•")
        if len(self.itens) > 0:
            for item in self.itens:
                status = "Disponível" if item.disponivel else "Alugado"
                print(f'- {item.codigo} | {item.titulo} ({status})')
            else:
                print("Nenhum item cadastrado")