import unittest
from calculos import soma, subtrai, divide, multiplica
from conversao import inteiro_para_romano, romano_para_inteiro

class TestCalculos(unittest.TestCase):
  def test_soma(self):
    self.assertEqual(soma(2, 3), 5)
    self.assertEqual(soma(-1, 1), 0)

  def test_subtrai(self):
    self.assertEqual(subtrai(5, 2), 3)
    self.assertEqual(subtrai(1, -1), 2)

  def test_divide(self):
    self.assertEqual(divide(10, 2), 5)
    self.assertEqual(divide(5, 0), "Erro: divisão por zero")

  def test_multiplica(self):
    self.assertEqual(multiplica(2, 3), 6)
    self.assertEqual(multiplica(-1, 1), -1)

class TestConversao(unittest.TestCase):
  def test_inteiro_para_romano(self):
    self.assertEqual(inteiro_para_romano(1), 'I')
    self.assertEqual(inteiro_para_romano(4), 'IV')
    self.assertEqual(inteiro_para_romano(10), 'X')
    self.assertEqual(inteiro_para_romano(42), 'XLII')
    self.assertEqual(inteiro_para_romano(1984), 'MCMLXXXIV')

  def test_romano_para_inteiro(self):
    self.assertEqual(romano_para_inteiro('I'), 1)
    self.assertEqual(romano_para_inteiro('IV'), 4)
    self.assertEqual(romano_para_inteiro('X'), 10)
    self.assertEqual(romano_para_inteiro('XLII'), 42)
    self.assertEqual(romano_para_inteiro('MCMLXXXIV'), 1984)

if __name__ == '__main__':
  unittest.main()