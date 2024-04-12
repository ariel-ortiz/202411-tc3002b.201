from delta import Compiler, Phase


source = '''
/* Este es
   un comentario */
   1
   + // otro comentario
   1
/* Comentario final */
'''

c = Compiler('program')
c.realize(source)
print()
print(c.parse_tree_str)
print()
print(c.wat_code)
print()
print(c.result)
