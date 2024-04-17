# File: tests/test_06_parenthesis.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestParenthesis(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake1(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('(1 + 2')

    def test_syntax_mistake2(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('(((((((42))))))))')

    def test_parenthesis1(self):
        self.assertEqual(3,
                         self.c.realize('(1+2)'))

    def test_parenthesis2(self):
        self.assertEqual(9,
                         self.c.realize('(1+2)*3'))

    def test_parenthesis3(self):
        self.assertEqual(12,
                         self.c.realize('(1+2)*(10-6)'))

    def test_parenthesis4(self):
        self.assertEqual(61,
                         self.c.realize(
                            '((((1) + (2) + (3)) * (10)) + (1))'))

    def test_parenthesis5(self):
        self.assertEqual(42,
                         self.c.realize('((((((((42))))))))'))
