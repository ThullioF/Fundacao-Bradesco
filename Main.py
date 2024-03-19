class Main:
    pass


print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente("João", "163706-6584")

conta = Conta(c1._nome, 6565, 0)

conta.deposita(100)
conta.saque(50)

print(conta._titular, " Número: ", conta._numero, " Seu saldo: ", conta.saldo)
