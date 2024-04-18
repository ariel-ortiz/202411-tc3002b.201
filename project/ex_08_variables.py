from delta import Compiler, Phase


source = '''

var x, y;         // First statement
x = 2;
y = (x + 1) * 3;
var z;
z = y - 1;        // Last statement
x + y + z         // Resulting expression


'''

c = Compiler('program')
c.realize(source)
# print()
# print(c.parse_tree_str)
print()
print(c.symbol_table)
print()
print(c.wat_code)
print()
print(c.result)
