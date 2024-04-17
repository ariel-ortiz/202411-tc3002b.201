# File: tests/test_07_unary.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestUnary(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake1(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('5-')

    def test_neg(self):
        self.assertEqual(-42,
                         self.c.realize('-42'))

    def test_pos(self):
        self.assertEqual(42,
                         self.c.realize('+42'))

    def test_not_false(self):
        self.assertEqual(1,
                         self.c.realize('!false'))

    def test_not_true(self):
        self.assertEqual(0,
                         self.c.realize('!true'))

    def test_not_0(self):
        self.assertEqual(1,
                         self.c.realize('!0'))

    def test_not_1(self):
        self.assertEqual(0,
                         self.c.realize('!1'))

    def test_not_42(self):
        self.assertEqual(0,
                         self.c.realize('!42'))

    def test_mix1(self):
        self.assertEqual(1,
                         self.c.realize('!!--+5'))

    def test_mix2(self):
        self.assertEqual(0,
                         self.c.realize('!!!--+5'))

    def test_mix3(self):
        self.assertEqual(-1,
                         self.c.realize('+-!!3'))

    def test_mix4(self):
        self.assertEqual(1,
                         self.c.realize('!!-+3'))
