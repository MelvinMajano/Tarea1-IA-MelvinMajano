


class CuentaBancaria:
    saldo=0
    def __init__(self, titular):
        self.titular=titular

    def depositar(self, valor):
        self.saldo+=valor

    def retirar(self, valor):
        if self.saldo==0:
            print('Su saldo esta en cero, por lo tanto no se puede realizar el retiro ')
        elif self.saldo<valor:
            print('Su saldo es insufficiente para realizar el retiro ')
        elif self.saldo>=valor:
            self.saldo-=valor

    def mostrar_saldo(self):
        return self.saldo

cuenta=CuentaBancaria('Melvin Majano')
print(f'Su saldo es: {cuenta.mostrar_saldo()}')
cuenta.depositar(100)
print(f'Su saldo es: {cuenta.mostrar_saldo()}')
cuenta.retirar(25)
print(f'Su saldo es: {cuenta.mostrar_saldo()}')
cuenta.retirar(100)
print(f'Su saldo es: {cuenta.mostrar_saldo()}')
cuenta.depositar(200)
print(f'Su saldo es: {cuenta.mostrar_saldo()}')
cuenta.retirar(275)
print(f'Su saldo es: {cuenta.mostrar_saldo()}')
cuenta.retirar(500)