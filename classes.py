
class Item:
    def __init__ (self, código: int, título: str):
        self.__codigo = código
        self.__titulo = título
        self.__disponivel = True 


    def Pegar(self):
        if self.__disponivel:
            self.__disponivel = False
            return True
        return False
            


    def Largar(self):
        if self.__disponivel:
            self.__disponivel = True
            return True
        return False
    
    
    def GetCódigo (self):
        return self.__codigo
    
    def GetTítulo (self):
        return self.__titulo


class Filme(Item):
    def __init__(self, código: int, título: str, gênero: str, duração: int):
        Item.__init__(self, código, título)
        self.__genero = gênero
        self.__duracao = duração

    def GetGênero (self):
        return self.__genero
    
    def GetDuração (self):
        return self.__duracao



class Jogo(Item):
    def __init__(self, código: int, título: str, plataforma: str, faixa_etária: int):
        Item.__init__(self, código, título)
        self.__plataforma = plataforma
        self.__faixaetaria = faixa_etária


    def GetPlataforma (self):
        return self.__plataforma
    
    def GetFaixaetaria (self):
        return self.__faixaetaria



class Cliente: #A classe Cliente deve ser capaz de locar e devolver itens
    def __init__(self, nome: str, cpf: str):
        self.__nome = nome
        self.__cpf = cpf
        self.__alugados = []


    def alugar(self, item:Item):
        if item.alugar():
            self.__itensAlugados.append(item)
            return True
        return False
    
    def devolução(self, item:Item):
        if item.devol():
            self.__itensAlugados.append(item)
            return True
        return False
    

    def listaritens(self):
        return [Item.titulo for item in self.__itensAlugados]
    
    
    def GetNome (self):
        return self.__nome
    
    def GetCpf (self):
        return self.__cpf


    def GetAlugados (self):
        return self.__ItensAlugados




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


    def GetClientes (self):
        return self.__clientes
    
    def GetItens (self):
        return self.__itens