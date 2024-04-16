# File: tests/test_03_additive.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestAdditive(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('1 +')

    def test_add1(self):
        self.assertEqual(3,
                         self.c.realize('1 + 2'))

    def test_add2(self):
        self.assertEqual(13,
                         self.c.realize('1 + 2 + 10'))

    def test_add3(self):
        self.assertEqual(55,
                         self.c.realize('1+2+3+4+5+6+7+8+9+10'))

    def test_sub1(self):
        self.assertEqual(3,
                         self.c.realize('10-7'))

    def test_sub2(self):
        self.assertEqual(-3,
                         self.c.realize('7-10'))

    def test_sub3(self):
        self.assertEqual(-13,
                         self.c.realize('1-2-3-4-5'))

    def test_sub4(self):
        self.assertEqual(-130,
                         self.c.realize('10-20-30-40-50'))

    def test_mix(self):
        self.assertEqual(50,
                         self.c.realize('10 + 20 - 30 + 40 - 50 + 60'))
