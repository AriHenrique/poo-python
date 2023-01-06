class ContaCorrente:

    def __init__(self, numero: int, titular, saldo: float, limite: float):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def cria_conta(self):
        conta = {'numero': self.__numero, 'titular': self.__titular, 'saldo': self.__saldo, 'limite': self.__limite}
        return conta

    def deposita(self, valor: float):
        self.__saldo += valor
        print(f'Foram depositados {valor}')

    def __pode_sacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def saque(self, valor: float):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
            print(f'Foi feito o saque de {valor}: saldo = {self.__saldo}')
        else:
            print(f'O valor {valor} é superior ao limite da conta: saldo {self.__saldo}\nlimite {self.__limite}')

    def extrato(self):
        print(f'Saldo do titular {self.__titular} é {self.__saldo}')

    def transferir(self, valor: float, destino):
        self.saque(valor)
        destino.deposita(valor)

    @property
    def get_saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite: float):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
