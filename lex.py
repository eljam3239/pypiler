class Lexer:
    def __init__(self, source):
        self.source = source + '\n' #append newline to simplify lexing
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def nexChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source[self.curPos]

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
