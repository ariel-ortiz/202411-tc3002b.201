from delta import Compiler, Phase


source = 'true'

c = Compiler('program')
c.realize(source)
print()
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)
