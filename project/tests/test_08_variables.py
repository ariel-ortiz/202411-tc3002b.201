# File: tests/test_08_variables.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from delta.semantics import SemanticMistake


class TestVariables(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('var x,')

    def test_vars0(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var var_1;
                            var var_2;
                            var var_3;
                            var_1 + var_2 + var_3
                            '''))

    def test_vars1(self):
        self.assertEqual(42,
                         self.c.realize(
                            '''
                            var x;
                            x = 42;
                            x
                            '''))

    def test_vars2(self):
        self.assertEqual(15,
                         self.c.realize(
                            '''
                            var x, y, z;
                            x = 2;
                            y = 8;
                            z = x * y - 1;
                            z
                            '''))

    def test_vars3(self):
        self.assertEqual(10,
                         self.c.realize(
                            '''
                            var a;
                            a = 10;
                            var b, c;
                            b = 100;
                            c = (b - a * 2) / 8;
                            c
                            '''))

    def test_vars4(self):
        self.assertEqual(55,
                         self.c.realize(
                            '''
                            var v, w, x, y, z;
                            v = 1;
                            w = 2;
                            x = 3;
                            y = 4;
                            z = 5;
                            var a, b, c, d, e;
                            a = 6;
                            b = 7;
                            c = 8;
                            d = 9;
                            e = 10;
                            a + b + c + d + e + v + w + x + y + z
                            '''))

    def test_vars5(self):
        self.assertEqual(19,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 2;
                            y = (x + 1) * 3;
                            var z;
                            z = y - 1;
                            x + y + z
                            '''))

    def test_duplicated_variable1(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize(
                '''
                var x, y, z;
                x = 10;
                var v, w, x;
                x
                ''')

    def test_duplicated_variable2(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize(
                '''
                var x, y, x;
                x = 10;
                x
                ''')

    def test_reserved_word(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize(
                '''
                var x, y, var;
                x = 1;
                y = 2;
                var = 3;
                x + y + var
                ''')

    def test_undeclared_lhs(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize(
                '''
                var x;
                y = 10;
                x
                ''')

    def test_undeclared_rhs(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize(
                '''
                var x;
                x = 10 + z;
                x
                ''')
