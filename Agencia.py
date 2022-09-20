from random import randint


class Agencia:

    def __init__(self, telefone, cnpj, numero):
        self.telefone = telefone
        self.cnpj = cnpj
        self.numero = numero
        self.clientes = []
        self.caixa = 0
        self.emprestimos = []

    def verificar_caixa(self):
        if self.caixa < 1000000:
            print('Caixa abaixo do nível recomendado. Caixa atual: {}'.format(self.caixa))
        else:
            print('O valor de caixa está OK. Caixa atual: {}'.format(self.caixa))

    def emprestar_dinheiro(self, valor, cpf, juros):
        if self.caixa > valor:
            self.emprestimos.append((valor, cpf, juros))
        else:
            print('Empréstimo não é possível. Dinheiro não disponível em caixa.')

    def adicionar_cliente(self, nome, cpf, patrimonio):
        self.clientes.append((nome, cpf, patrimonio))


class AgenciaVirtual(Agencia):

    def __init__(self, site, telefone, cnpj):
        self.site = site
        super().__init__(telefone, cnpj, 1000) #Puxa o método init da classe "mãe", caso contrário, o método init da subclasse, substitui o da classe "mãe"
        self.caixa = 1000000
        self.caixa_paypal = 0


    def depositar_paypal(self, valor):
        self.caixa -= valor
        self.caixa_paypal += valor


    def sacar_paypal(self, valor):
        self.caixa_paypal -= valor
        self.caixa += valor


class AgenciaComum(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 1000000


class AgenciaPremium(Agencia):

    def __init__(self, telefone, cnpj):
        super().__init__(telefone, cnpj, numero=randint(1001, 9999))
        self.caixa = 10000000


    def adicionar_cliente(self, nome, cpf, patrimonio): #Muda a forma de como esse método já existente na classe "mãe" funcionará nessa subclasse
        if patrimonio > 1000000: #Substitui o método adicionar_cliente da classe "mãe" para funcionar da forma que a subclasse AgenciaPremium precisa.
            super().adicionar_cliente(nome, cpf, patrimonio) #Usa o método adicionar_cliente que está na classe "mãe" (mesma coisa do init)
        else:
            print('O cliente não possui patrimônio suficiente para entrar na agência.')



#if __name__ == '__main__': ---> Tudo que for colocado dentro do if, não vai ser executado numa importação.
