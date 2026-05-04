import unittest
from server.filtro import filtrar_livros
from livros_data import livros

class TestFiltro(unittest.TestCase):

    def test_autor(self):
        resultado = filtrar_livros(livros, autor="Machado")
        self.assertTrue(len(resultado) > 0)

    def test_genero(self):
        resultado = filtrar_livros(livros, genero="Romance")
        self.assertTrue(len(resultado) > 0)

    def test_ano(self):
        resultado = filtrar_livros(livros, ano="1937")
        for livro in resultado:
            self.assertEqual(livro["ano"], 1937)

    def test_multiplos(self):
        resultado = filtrar_livros(livros, autor="Machado", genero="Romance")
        for livro in resultado:
            self.assertIn("machado", livro["autor"].lower())

    def test_vazio(self):
        resultado = filtrar_livros(livros, titulo="NadaExiste")
        self.assertEqual(len(resultado), 0)

if __name__ == "__main__":
    unittest.main()