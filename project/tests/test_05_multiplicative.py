# File: tests/test_05_multiplicative.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from wasmtime._trap import Trap


class TestMultiplicative(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('* 2')

    def test_mul1(self):
        self.assertEqual(33,
                         self.c.realize('3 * 11'))

    def test_mul2(self):
        self.assertEqual(100,
                         self.c.realize('10 * 5 * 2'))

    def test_div1(self):
        self.assertEqual(6,
                         self.c.realize('20 / 3'))

    def test_div2(self):
        self.assertEqual(0,
                         self.c.realize('25 / 100'))

    def test_div3(self):
        self.assertEqual(2,
                         self.c.realize('100 / 4 / 10'))

    def test_div_by_zero(self):
        with self.assertRaises(Trap):
            self.c.realize('25 / 0')

    def test_rem1(self):
        self.assertEqual(2,
                         self.c.realize('20 % 3'))

    def test_rem2(self):
        self.assertEqual(7,
                         self.c.realize('100 % 40 % 13'))

    def test_rem_by_zero(self):
        with self.assertRaises(Trap):
            self.c.realize('10 % 0')

    def test_mix1(self):
        self.assertEqual(
            7,
            self.c.realize('1 + 2 * 3')
        )

    def test_mix2(self):
        self.assertEqual(
            -1,
            self.c.realize('3 + 10 * 5 - 10 / 4 * 20 % 15 + 4 * 9 - 80')
        )
