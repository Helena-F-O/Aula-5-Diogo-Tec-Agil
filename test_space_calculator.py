import unittest
from space_calculator import Converter


class TestConverter(unittest.TestCase):

  def setUp(self):
    self.calculator = Converter()

  def test_converter_massa_lunar(self):
    # Teste de conversão de quilogramas para massa lunar
    self.assertAlmostEqual(self.calculator.converter_massa_lunar(100),
                           16.53,
                           places=2)

  def test_converter_distancia_marte(self):
    # Teste de conversão de metros para distância em Marte
    self.assertAlmostEqual(self.calculator.converter_distancia_marte(1000),
                           377.30,
                           places=2)


if __name__ == '__main__':
  unittest.main()
