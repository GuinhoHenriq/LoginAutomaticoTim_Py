class Usuario:
    def __init__(self, nome, matricula, ip, login):
        self.nome = nome
        self.matricula = matricula
        self.ip = ip
        self.login = login

#NOME
    @property
    def nome(self):
         # Este código é executado quando alguém for
         # ler o valor de self.nome
         return self._nome

    @nome.setter
    def nome(self, value):
         # este código é executado sempre que alguém fizer 
         # self.nome = value
         self._nome = value

#MATRICULA
    @property
    def matricula(self):
         # Este código é executado quando alguém for
         # ler o valor de self.matricula
         return self._matricula

    @matricula.setter
    def matricula(self, value):
         # este código é executado sempre que alguém fizer 
         # self.matricula = value
         self._matricula = value

#IP
    @property
    def ip(self):
         # Este código é executado quando alguém for
         # ler o valor de self.ip
         return self._ip

    @ip.setter
    def ip(self, value):
         # este código é executado sempre que alguém fizer 
         # self.ip = value
         self._ip = value

#LOGIN  
    @property
    def login(self):
         # Este código é executado quando alguém for
         # ler o valor de self.login
         return self._login

    @login.setter
    def login(self, value):
         # este código é executado sempre que alguém fizer 
         # self.login = value
         self._login = value


