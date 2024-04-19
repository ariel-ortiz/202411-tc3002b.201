# File: tests/test_10_while.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from delta.semantics import SemanticMistake


class TestWhile(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('while {}')

    def test_semantic_mistake(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var while; 0')

    def test_while_zero(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var x, y;
                            x = 0;
                            y = 0;
                            while x {
                                x = x - 1;
                                y = 1;
                            }
                            x + y
                            '''))

    def test_while_fact(self):
        self.assertEqual(120,
                         self.c.realize(
                            '''
                            var n, r, i;
                            n = 5;
                            r = 1;
                            i = 0;
                            while n - i {
                                i = i + 1;
                                r = r * i;
                            }
                            r
                            '''))

    def test_while_count_down(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var i;
                            i = 10;
                            while i {
                                i = i - 1;
                            }
                            i
                            '''))

    def test_while_skip_body(self):
        self.assertEqual(10,
                         self.c.realize(
                            '''
                            var n;
                            n = 10;
                            while !n {
                                n = n - 1;
                            }
                            n
                            '''))

    def test_while_fibo(self):
        self.assertEqual(55,
                         self.c.realize(
                            '''
                            var n, a, b;
                            n = 10;
                            a = 0;
                            b = 1;
                            while n {
                                var t;
                                t = b;
                                b = a + b;
                                a = t;
                                n = n - 1;
                            }
                            a
                            '''))

    def test_while_nested(self):
        self.assertEqual(1500,
                         self.c.realize(
                            '''
                            var r, i;
                            r = 0;
                            i = 10;
                            while i {
                                var j;
                                j = 50;
                                while j {
                                    var k;
                                    k = 3;
                                    while k {
                                        r = r + 1;
                                        k = k - 1;
                                    }
                                    j = j - 1;
                                }
                                i = i - 1;
                            }
                            r
                            '''))
