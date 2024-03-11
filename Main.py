class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João","163706-6584")

conta = Conta(c1.nome,6565,0)

print(conta.titular, " Núm ero: ",conta.numero, " Seu saldo: ",conta.saldo)