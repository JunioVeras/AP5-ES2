import unittest
import math
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calculadora = Calculadora()

    def test_adicionar_positivos(self):
        self.assertEqual(self.calculadora.adicionar(3, 4), 7)

    def test_adicionar_nagativos(self):
        self.assertEqual(self.calculadora.adicionar(-3, -2), -5)

    def test_adicionar_positivo_negativo(self):
        self.assertEqual(self.calculadora.adicionar(3, -3), 0)
        self.assertEqual(self.calculadora.adicionar(-2, 7), 5)

    def test_subtrair_positivos(self):
        self.assertEqual(self.calculadora.subtrair(8, 4), 4)

    def test_subtrair_nagativos(self):
        self.assertEqual(self.calculadora.subtrair(-8, -4), -4)

    def test_subtrair_positivo_negativo(self):
        self.assertEqual(self.calculadora.subtrair(8, -4), 12)
        self.assertEqual(self.calculadora.subtrair(-3, 5), -8)

    def test_multiplicar_positivos(self):
        self.assertEqual(self.calculadora.multiplicar(2, 6), 12)

    def test_multiplicar_nagativos(self):
        self.assertEqual(self.calculadora.multiplicar(-2, -6), 12)

    def test_multiplicar_positivo_negativo(self):
        self.assertEqual(self.calculadora.multiplicar(2, -6), -12)
        self.assertEqual(self.calculadora.multiplicar(-2, 6), -12)

    def test_dividir_positivos(self):
        self.assertEqual(self.calculadora.dividir(10, 2), 5)

    def test_dividir_nagativos(self):
        self.assertEqual(self.calculadora.dividir(-10, -2), 5)

    def test_dividir_positivo_negativo(self):
        self.assertEqual(self.calculadora.dividir(-10, 2), -5)
        self.assertEqual(self.calculadora.dividir(10, -2), -5)

    def test_dividir_0(self):
        self.assertTrue(math.isnan(self.calculadora.dividir(5, 0)))

    def test_elevar_positivos(self):
        self.assertEqual(self.calculadora.elevar(10, 2), 100)

    def test_elevar_negativos(self):
        self.assertEqual(self.calculadora.elevar(-10, -2), 0.01)

    def test_elevar_positivo_negativo(self):
        self.assertEqual(self.calculadora.elevar(10, -2), 0.01)
        self.assertEqual(self.calculadora.elevar(-10, 2), 100)

    def test_elevar_0(self):
        self.assertEqual(self.calculadora.elevar(10, 0), 1)

if __name__ == '__main__':
    unittest.main()