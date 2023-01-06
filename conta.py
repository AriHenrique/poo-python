class ContaCorrente:

    def __init__(self, numero: int, titular, saldo: float, limite: float):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def cria_conta(self):
        conta = {'numero': self.__numero, 'titular': self.__titular, 'saldo': self.__saldo, 'limite': self.__limite}
        return conta

    def deposita(self, valor: float):
        self.__saldo += valor
        print(f'Foram depositados {valor}')

    def saque(self, valor: float):
        self.__saldo -= valor
        print(f'Foi feito o saque de {valor}')

    def extrato(self):
        print(f'Saldo do titular {self.__titular} é {self.__saldo}')

    def transferir(self, valor: float, destino):
        self.saque(valor)
        destino.deposita(valor)

    def teste(self):
        print('aqui')
