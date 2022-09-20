from Conta_Corrente import ContaCorrente
from Cartao_Credito import CartaoCredito
from Agencia import AgenciaComum, AgenciaVirtual, AgenciaPremium


#----------Criando as contas correntes------------
conta_victor = ContaCorrente('Victor', '111.222.333-44', 1234, 34062)
conta_mae_do_victor = ContaCorrente('Veronica', '555.666.777-88', 5678, 34532)

#Depositando dinheiro na conta Victor
conta_victor.depositar(10000)

#Sacar dinheiro da conta Victor
#conta_victor.sacar_dinheiro(10500)

#Consultando saldo da conta Victor
conta_victor.consultar_saldo()
print('-' * 20)

#Consultando limite do cheque especial da conta Victor
conta_victor.consultar_limite_cheque_especial()
print('-' * 20)

#Consultando histórico de transações da conta Victor
conta_victor.consultar_historico_transacoes()

#Tranferindo dinheiro da conta Victor para a conta mãe do Victor
conta_victor.transferir(1000, conta_mae_do_victor)

#Consultando saldo de ambas as contas
conta_victor.consultar_saldo()
conta_mae_do_victor.consultar_saldo()


#Consultando histórico de transações de ambas as contas
conta_victor.consultar_historico_transacoes()
conta_mae_do_victor.consultar_historico_transacoes()


#-----------Criação do cartão----------
cartao_victor = CartaoCredito('Victor', conta_victor)

#Número da conta corrente vinculada ao cartão Victor
print(cartao_victor.conta_corrente._num_conta)

#Consultando a validade do cartão Victor
print(conta_victor.cartoes[0].validade )
#  OU
print(cartao_victor.validade)

#Consultando o número do cartão Victor
print(cartao_victor.numero)

#Consultando o código de segurança do cartão Victor
print(cartao_victor.cod_seguranca)

#Criando e consultando a senha do cartão Victor
cartao_victor.senha = '1244'
print(cartao_victor.senha)

#Consultando todos os atributos adquiridos da conta Victor
print(conta_victor.__dict__) #--> Consultar todos valores da instância da classe (atributos,etc)


#--------------Criação da agência virtual e verificando quanto tem em caixa
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 22224444, 15200000000)
agencia_virtual.verificar_caixa()

#Consultando o site da agência virtual
print(agencia_virtual.site)

#Depositando uma quantia de dinheiro do caixa da agência virtual no caixa da plataforma Paypal e consultando o quanto tem em caixa da agência virtual e quanto tem no caixa do Paypal
agencia_virtual.depositar_paypal(20000)
print(agencia_virtual.caixa)
print(agencia_virtual.caixa_paypal)


#--------------Criação da agência comum e verificando quanto tem em caixa
agencia_comum = AgenciaComum(22225555, 25500000000)
agencia_comum.verificar_caixa()

##Adicionando cliente na agência comum e consultando os clientes
agencia_comum.adicionar_cliente('Irmão do lira', 10200000000, 10)
print(agencia_comum.clientes)

#--------------Criação da agência premium e verificando quanto tem em caixa
agencia_premium = AgenciaPremium(22226666, 55500000000)
agencia_premium.verificar_caixa()

#Adicionando cliente na agência premium e consultando os clientes
agencia_premium.adicionar_cliente('Lira', 15000000000, 50000000)
print(agencia_premium.clientes)


