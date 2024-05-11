class Lexer:
    def __init__(self, source):
        self.source = source + '\n' #append newline to simplify lexing
        self.curChar = ''
        self.curPos = -1
        self.nextChar()

    def nextChar(self):
        self.curPos += 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source[self.curPos]
    
    #return the lookahead character
    def peek(self):
        if self.curPos + 1 >= len(self.source):
            return '\0'
        return self.source[self.curPos+1]
        

    #invalid token, exit
    def abort(self, message):
        pass

    def skipWhiteSpace(self):
        pass

    def skipComment(self):
        pass

    def getToken(self):
        if self.curChar == '+':
            pass
        elif self.curChar == '-':
            pass
        elif self.curChar == '*':
            pass
        elif self.curChar == '/':
            pass
        elif self.curChar == '\n':
            pass
        elif self.curChar == '\0':
            pass
        else:
            pass
        

        self.nextChar()
