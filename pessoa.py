class Pessoa:
    def __init__(self, nome, email, senha, contato, endereco, cpf, genero):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.contato = contato
        self.endereco = endereco
        self.cpf = cpf
        self.genero = genero

    @property       #recuperacão
    def nome(self):
        return self._nome

    @nome.setter        #atualizacão
    def nome(self, nome):
        self._nome = nome

    @property       #recuperacão
    def email(self):
        return self._email

    @email.setter        #atualizacão
    def email(self, email):
        self._email = email

    @property       #recuperacão
    def senha(self):
        return self._senha

    @senha.setter        #atualizacão
    def senha(self, senha):
        self._senha = senha

    @property       #recuperacão
    def contato(self):
        return self._contato

    @contato.setter        #atualizacão
    def contato(self, contato):
        self._contato = contato 

    @property       #recuperacão
    def endereco(self):
        return self._endereco

    @endereco.setter        #atualizacão
    def endereco(self, endereco):
        self._endereco = endereco

    @property       #recuperacão
    def cpf(self):
        return self._cpf

    @cpf.setter        #atualizacão
    def cpf(self, cpf):
        self._cpf = cpf

    @property       #recuperacão
    def genero(self):
        return self._genero

    @genero.setter        #atualizacão
    def genero(self, genero):
        self._genero = genero
    

    def Falar(self):
        print("bla bla bla...")

    def Ouvir(self):
        print("ouvindo....")

    def Andar(self):
        print("andando...")

    def Informacoes_pessoa(self):

        nome = "Benedita"
        email = "benedita5587988558672@gmail.com"
        senha = "WhP0952b"
        contato = "(87) 98855-8672"
        endereco = "Dom Avelar, Rua da Ametista, 180"
        cpf = "111.111.11-11"
        genero = "Feminino"

        print("Nome:", nome)
        print("Email: ", email)
        print("senha: ****** ")
        print("Contato: ", contato)
        print("Endereco: ", endereco)
        print("CPF:", cpf)
        print("Gênero:", genero)

    def Registrar_pessoa(self):

        print("-----REGISTRANDO PESSOA-----")
        nome = input("Nome: ")
        email = input("E-mail:")
        senha = input("Senha: ") 
        contato = input("Digite seu Contato:")
        endereco = input("Digite seu endereco: ")
        cpf = input("Digite seu cpf: ")
        genero = input("Digite seu genero: ")

        print("Nome:", nome)
        print("Email: ", email)
        print("senha: ****** ")
        print("Contato: ", contato)
        print("Endereco: ", endereco)
        print("CPF:", cpf)
        print("Gênero:", genero)



p1 = Pessoa('', '', '', '', '', '', '')
#p1.Falar()
#p1.Ouvir()
#p1.Andar()
#p1.Informacoes_pessoa()
p1.Registrar_pessoa()