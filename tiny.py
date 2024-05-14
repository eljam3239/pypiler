from lex import *
from parse import *
import sys


def main():
    print("Compiler")
    
    if len(sys.argv) != 2:
        sys.exit("Error: Compiler needs source file")
    with open(sys.argv[1],'r') as inputFile:
        source = inputFile.read()

    lexer = Lexer(source)
    parser = Parser(source)
    
    parser.program()
    print("Parsing completed")

main()