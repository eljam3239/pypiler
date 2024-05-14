import sys
from lex import *

class Parser:
    def __init__(self, lexer):
        pass
    
    def checkToken(self, kind):
        pass

    def checkPeek(self, kind):
        pass

    def match(self, kind):
        pass

    def nextToken(self):
        pass

    def abort(self, message):
        sys.exit("Error. " + message)