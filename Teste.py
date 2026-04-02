import unittest
from filtro import filtrar_livros
from dicionari import livros

class TestFiltroLivros(unittest.TestCase):

    def test_filtrar_por_autor(self):
        resultado = filtrar_livros(livros, autor="George Orwell")
        self.assertEqual(len(resultado), 2)

    def test_filtrar_por_genero(self):
        resultado = filtrar_livros(livros, genero="Fantasia")
        self.assertEqual(len(resultado), 2)

    def test_filtrar_por_ano(self):
        resultado = filtrar_livros(livros, ano=1954)
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "O Senhor dos Anéis")

    def test_filtrar_por_titulo(self):
        resultado = filtrar_livros(livros, titulo="Dom Casmurro")
        self.assertEqual(len(resultado), 1)

    def test_filtrar_por_tudo(self):
        resultado = filtrar_livros(
            livros,
            autor="Machado de Assis",
            genero="Romance",
            ano=1899
        )
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "Dom Casmurro")

if __name__ == "__main__":
    unittest.main()