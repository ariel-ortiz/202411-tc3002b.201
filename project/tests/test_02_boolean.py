# File: tests/test_02_boolean.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestBoolean(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('true.')

    def test_true(self):
        self.assertEqual(1,
                         self.c.realize('true'))

    def test_false(self):
        self.assertEqual(0,
                         self.c.realize('false'))
