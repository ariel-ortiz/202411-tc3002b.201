from enum import Enum
from os import path
from arpeggio import visit_parse_tree, NoMatch
from arpeggio.cleanpeg import ParserPEG
from wasmtime import Store, Module, Instance
from delta.codegen import CodeGenerationVisitor
from delta.semantics import SemanticVisitor


class SyntaxMistake(Exception):

    def __init__(self, exception):
        super().__init__(f'Syntax error: {exception}')


class Phase(Enum):
    SYNTACTIC_ANALYSIS = 1
    SEMANTIC_ANALYSIS = 2
    CODE_GENERATION = 3
    EVALUATION = 4


class Compiler:

    PEG_FILE = 'delta.peg'

    def __init__(self, root_rule):
        self.__root_rule = root_rule
        self.__peg_file = path.join(path.dirname(__file__),
                                    Compiler.PEG_FILE)
        self.__parser = None
        self.__parse_tree = None
        self.__symbol_table = None
        self.__wat_code = None
        self.__result = None

    def realize(self, source_code, phase=Phase.EVALUATION):

        def create_parser():
            with open(self.__peg_file) as file:
                grammar = file.read()
            return ParserPEG(grammar, self.__root_rule)

        def syntax_analysis():
            try:
                return self.__parser.parse(source_code)
            except NoMatch as e:
                raise SyntaxMistake(e)

        def semantic_analysis():
            semantic_visitor = SemanticVisitor(self.__parser)
            visit_parse_tree(self.__parse_tree, semantic_visitor)
            return semantic_visitor.symbol_table

        def generate_wat_code():
            code_visitor = CodeGenerationVisitor(self.__symbol_table)
            return visit_parse_tree(self.__parse_tree, code_visitor)

        def execute_wasm_start_function():
            store = Store()
            module = Module(store.engine, self.__wat_code)
            instance = Instance(store, module, [])
            start_function = instance.exports(store)['_start']
            return start_function(store)

        self.__parser = create_parser()
        self.__parse_tree = syntax_analysis()
        if phase.value >= Phase.SEMANTIC_ANALYSIS.value:
            self.__symbol_table = semantic_analysis()
        if phase.value >= Phase.CODE_GENERATION.value:
            self.__wat_code = generate_wat_code()
        if phase.value == Phase.EVALUATION.value:
            self.__result = execute_wasm_start_function()
        return self.__result

    @property
    def parse_tree_str(self):
        if self.__parse_tree is None:
            raise ValueError('No parse tree currently available')
        return self.__parse_tree.tree_str()

    @property
    def symbol_table(self):
        if self.__symbol_table is None:
            raise ValueError('No symbol table currently available')
        return self.__symbol_table

    @property
    def wat_code(self):
        if self.__wat_code is None:
            raise ValueError('No WAT code currently available')
        return self.__wat_code

    @property
    def result(self):
        if self.__result is None:
            raise ValueError('No result currently available')
        return self.__result
