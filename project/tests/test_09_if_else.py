# File: tests/test_09_if_else.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake
from delta.semantics import SemanticMistake


class TestIfElse(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('if true {')

    def test_semantic_mistake1(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var if; 0')

    def test_semantic_mistake2(self):
        with self.assertRaises(SemanticMistake):
            self.c.realize('var else; 0')

    def test_if(self):
        self.assertEqual(11,
                         self.c.realize(
                            '''
                            var x;
                            x = 10;
                            if true {
                                x = x + 1;
                            }
                            x
                            '''))

    def test_if_else_1(self):
        self.assertEqual(2,
                         self.c.realize(
                            '''
                            var x;
                            x = 1;
                            if true {
                                x = x * 2;
                            } else {
                                x = x + 2;
                            }
                            x
                            '''))

    def test_if_else_2(self):
        self.assertEqual(3,
                         self.c.realize(
                            '''
                            var x;
                            x = 1;
                            if false {
                                x = x * 2;
                            } else {
                                x = x + 2;
                            }
                            x
                            '''))

    def test_if_else_3(self):
        self.assertEqual(1,
                         self.c.realize(
                            '''
                            var x;
                            x = true;
                            if x {
                            } else {
                            }
                            x
                            '''))

    def test_if_else_4(self):
        self.assertEqual(0,
                         self.c.realize(
                            '''
                            var x;
                            x = false;
                            if x {
                            } else {
                            }
                            x
                            '''))

    def test_if_else_5(self):
        self.assertEqual(38,
                         self.c.realize(
                            '''
                            var a, b, c;
                            a = 1;
                            b = 2;
                            c = 3;
                            if a + b - c {
                                a = a * 2;
                                b = b * 3;
                                c = c * 4;
                            } else {
                                a = a * 5;
                                b = b * 6;
                                c = c * 7;
                            }
                            a + b + c
                            '''))

    def test_if_else_6(self):
        self.assertEqual(20,
                         self.c.realize(
                            '''
                            var a, b, c;
                            a = 1;
                            b = 2;
                            c = 3;
                            if -1 + a + b - c {
                                a = a * 2;
                                b = b * 3;
                                c = c * 4;
                            } else {
                                a = a * 5;
                                b = b * 6;
                                c = c * 7;
                            }
                            a + b + c
                            '''))
