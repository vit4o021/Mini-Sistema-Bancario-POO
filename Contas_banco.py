from datetime import datetime
import pytz


class ContaCorrente:

    @staticmethod
    def _data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta) :
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0
        self.limite = None
        self.agencia = agencia
        self.num_conta = num_conta
        self.transacoes = []

    def consultar_saldo(self):
        print('Seu saldo atual é de R${:,.2f}'.format(self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append((valor, self.saldo, ContaCorrente._data_hora()))

    def _limite_conta(self):
        self.limite = -1000
        return self.limite

    def sacar_dinheiro(self, valor):
        if self.saldo - valor < self._limite_conta() :
            print('Você não tem saldo suficiente para sacar essa valor.')
            self.consultar_saldo()
        else:
            self.saldo -= valor
            self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))

    def consultar_limite_cheque_especial(self):
        print('Seu limite de cheque especial é de R${:,.2f}.'.format(self._limite_conta()))

    def consultar_historico_transacoes(self):
        print('Histórico de transações: ')
        for transacao in self.transacoes:
            print(transacao)

    def transferir(self, valor, conta_destino):
        self.saldo -= valor
        self.transacoes.append((-valor, self.saldo, ContaCorrente._data_hora()))
        conta_destino.saldo += valor
        conta_destino.transacoes.append((valor, conta_destino.saldo, ContaCorrente._data_hora()))


#Programa

#Criando as contas
conta_victor = ContaCorrente('Victor', '111.222.333-44', 1234, 34062)
conta_mae_do_victor = ContaCorrente('Veronica', '555.666.777-88', 5678, 34532)

#Depositando dinheiro na conta Victor
conta_victor.depositar(10000)

#sacar dinheiro da conta Victor
#conta_victor.sacar_dinheiro(10500)

#Consultando saldo da conta Victor
conta_victor.consultar_saldo()
print('-' * 20)

#Consultando limite do cheque especial
conta_victor.consultar_limite_cheque_especial()
print('-' * 20)

#Consultando histórico de transações da conta Victor
conta_victor.consultar_historico_transacoes()
print('-' * 20)

#Tranferindo dinheiro da conta Victor para a conta mãe do Victor
conta_victor.transferir(1000, conta_mae_do_victor)

#Consultando saldo de ambas as contas
conta_victor.consultar_saldo()
conta_mae_do_victor.consultar_saldo()
print('-' * 20)

#Consultando histórico de transações de ambas as contas
conta_victor.consultar_historico_transacoes()
conta_mae_do_victor.consultar_historico_transacoes()