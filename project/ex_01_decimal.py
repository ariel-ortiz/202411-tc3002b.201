from delta import Compiler, Phase


source = '8'

c = Compiler('program')
c.realize(source)
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)
