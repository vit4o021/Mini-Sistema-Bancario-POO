from datetime import datetime
import pytz


class ContaCorrente:
    """"
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes.

    Atributos:
        nome (str): Nome do cliente.
        cpf (str): CPF do cliente. Deve ser inserido com pontos e traços.
        agencia: Agência responsável pela conta do cliente.
        num_conta: Número da conta corrente do cliente.
        saldo: Saldo disponível na conta do cliente.
        limite: Limite de cheque especial daquele cliente.
        transacoes: Histórico de transações do cliente.
    """


    @staticmethod # --> sinalização para indicar que é um método estático/auxiliar.
    def _data_hora(): #método estático --> é um método que não vai usar nada da classe. Logo, não precisa de self.
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta) :
        self.nome = nome
        self.cpf = cpf
        self._saldo = 0 # --> O "_" na frente significa que é um método que não é para ser usado dentro do programa (Atributo não público)
        self._limite = None # e sim como um auxiliar para outros métodos da classe, ou seja, ele é usado somente dentro da classe. A única forma de consultá-lo é por meio dos métodos.
        self._agencia = agencia # Usando --> self.__agencia = agencia --> O "__" na frente faz com que esse atributo seja inacessível fora do programa, logo não pode ser consultado,
        self._num_conta = num_conta # a não ser que seja por meio dos métodos.
        self._transacoes = []
        self.cartoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self._saldo))

    def depositar(self, valor):
        self._saldo += valor
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def _limite_conta(self): # --> O "_" na frente significa que é um método que não é para ser usado dentro do programa (Método não público)
        self._limite = -1000  # e sim como um auxiliar para outros métodos da classe, ou seja, ele é usado somente dentro da classe. A única forma de consultá-lo é por meio dos métodos.
        return self._limite

    def sacar_dinheiro(self, valor):
        if self._saldo - valor < self._limite_conta() :
            print('Você não tem saldo suficiente para sacar essa valor.')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}.'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de transações: ')
        for transacao in self._transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


