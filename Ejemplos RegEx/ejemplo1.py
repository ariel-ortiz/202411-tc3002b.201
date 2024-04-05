import re


FILE_NAME = 'entrada.txt'


def main ():
    with open(FILE_NAME, 'r') as archivo:
        info = archivo.read()
        
        words = re.findall(r"(?:\w|')+", info)
        
        print (words)

if __name__ == '__main__':
    main()    