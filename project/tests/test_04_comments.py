# File: tests/test_04_comments.py

from unittest import TestCase
from delta import Compiler, SyntaxMistake


class TestComment(TestCase):

    def setUp(self):
        self.c = Compiler('program')

    def test_syntax_mistake(self):
        with self.assertRaises(SyntaxMistake):
            self.c.realize('/* this is comment')

    def test_line_comment(self):
        self.assertEqual(0,
                         self.c.realize('// this is a comment\n0'))

    def test_block_comment1(self):
        self.assertEqual(0,
                         self.c.realize('/* this is a comment */\n0'))

    def test_block_comment2(self):
        self.assertEqual(0,
                         self.c.realize(
                             '/* this\nis\na\ncomment */\n0'))

    def test_mix(self):
        self.assertEqual(2,
                         self.c.realize(
                             '''
                             /* first comment */
                             1
                             // second comment
                             +
                             // third
                             1
                             /*
                                fourth
                                comment
                             */
                             '''))
