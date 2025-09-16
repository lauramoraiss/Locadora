# PROJETO LOCADORA

### Explicação do código da subpasta por partes -> classe.py


![Image](https://github.com/user-attachments/assets/7060fd67-1226-4670-9744-07fccf5179b4)


**Para o início da criação do código foi necessário realizar a criação de classes para facilitar o desenvolvimento do código, assim também como para ficar uma organização maior e mais agradável** <br>

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


      def locar (self, item:Item):
            item.alugar()
            self.__alugados.append(item)


      def devolver (self, item:Item):
        if item in self.__alugados:
            item.devolver()
            self.__alugados.remove(item)
            return True
        return False


      def listaritens(self):
        return [Item.titulo for item in self.__alugados]
    
    
      def GetNome (self):
        return self.__nome
    
      def GetCpf (self):
        return self.__cpf


      def GetAlugados (self):
        return self.__alugados



![Image](https://github.com/user-attachments/assets/7060fd67-1226-4670-9744-07fccf5179b4)


## Explicação do código da subpasta por partes -> func.py


![Image](https://github.com/user-attachments/assets/7060fd67-1226-4670-9744-07fccf5179b4)


**pppppppppppppppppppppppppppppppppppppppppppppppppppppppp** <br>

(código)


![Image](https://github.com/user-attachments/assets/7060fd67-1226-4670-9744-07fccf5179b4)


## Explicação do código da subpasta por partes -> app.py


![Image](https://github.com/user-attachments/assets/7060fd67-1226-4670-9744-07fccf5179b4)


**ppppppppppppppppppppppppppppppppppppp** <br>

(código)
