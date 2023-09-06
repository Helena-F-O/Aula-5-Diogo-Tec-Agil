import unittest

from library4 import Biblioteca


class TestBiblioteca(unittest.TestCase):

  def setUp(self):
    self.biblioteca = Biblioteca()

  def test_adicionar_livro(self):
    self.biblioteca.adicionar_livro("Duna")
    self.assertEqual(self.biblioteca.listar_livros(), ["Duna"])

  def test_remover_livro(self):
    self.biblioteca.adicionar_livro("Duna")
    self.biblioteca.remover_livro("Duna")
    self.assertEqual(self.biblioteca.listar_livros(), [])

  def test_listar_livros(self):
    self.biblioteca.adicionar_livro("Duna")
    self.biblioteca.adicionar_livro("Neuromancer")
    self.assertEqual(self.biblioteca.listar_livros(), ["Duna", "Neuromancer"])


if __name__ == '__main__':
  unittest.main()
