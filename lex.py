class Lexer:
    def __init__(self, source):
        self.source = source + '\n' #append newline to simplify lexing
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def nexChar(self):
        pass

    def peek(self):
        pass

    #invalid token, exit
    def abort(self, message):
        pass

    def skipWhiteSpace(self):
        pass

    def skipComment(self):
        pass

    def getToken(self):
        pass
