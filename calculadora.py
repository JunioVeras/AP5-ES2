# comentario de teste
import math

class Calculadora:
    def adicionar(self, numero1, numero2):
        return numero1 + numero2

    def subtrair(self, numero1, numero2):
        return numero1 - numero2

    def multiplicar(self, numero1, numero2):
        return numero1 * numero2

    def dividir(self, numero1, numero2):
        if numero2 != 0:
            return numero1 / numero2
        else:
            return math.nan
    def elevar(self, numero1, numero2):
        return numero1 ** numero2