from delta import Compiler, Phase


source = '10 && 20 && 30 && 40 && 50'

c = Compiler('program')
c.realize(source)
print()
# print(c.parse_tree_str)
# print()
# print(c.symbol_table)
# print()
print(c.wat_code)
print()
print(c.result)
