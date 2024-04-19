from delta import Compiler, Phase


source = '''

var n, r, i;
n = 5;
r = 1;
i = 0;
while n - i {
    i = i + 1;
    r = r * i;
}
r

'''

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
