class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo  objeto")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f"Saldo {self.__saldo} do titular {self.__titular}")
    
    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            return (f"O valor {valor} ultrapassa o limite")

    def __pode_sacar(self, valor):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor <= valor_disponivel_a_sacar
    
    def  transfere(self, valor, conta):
        self.saca(valor)
        conta.deposita(valor)

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {'BB':'001', 'Caixa' : '101', 'Bradesco': '237'}
