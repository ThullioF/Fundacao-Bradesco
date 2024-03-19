class Conta:
    def __init__(self, titular, numero, saldo):

        self._saldo = saldo
        self._numero = numero
        self._titular = titular

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self,saldo):
            if (saldo < 0):
                print("O saldo não pode ser natgativo")
            else:
                self._saldo = saldo

    def deposita(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso")
        else:
            print("Valor do depósito deve ser maior que zero")

    def saque(self, valor):
        if (self.saldo >= valor):
            self._saldo -= valor
            print("Saque realizado com sucesso")
        else:
            print("saldo insuficiente")

    def extrato(self):
        print("Cliente: ", self._titular, " Saldo atual: ", self._saldo)

    @property
    def saldo(self):
        return self._saldo