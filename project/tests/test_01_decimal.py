# File: tests/test_01_decimal.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from delta.semantics import SemanticMistake


class TestIntLiteral(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('$1')

    def test_0(self):
        self.assertEqual(
            0,
            self.c.realize('0'))

    def test_42(self):
        self.assertEqual(
            42,
            self.c.realize('42'))

    def test_1000000(self):
        self.assertEqual(
            1000000,
            self.c.realize('1000000'))

    def test_max_int(self):
        self.assertEqual(
            2147483647,
            self.c.realize('2147483647'))

    def test_int_overflow(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('2147483648')

    def test_int_huge_overflow(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('340282366920938463463374607431768211455')
