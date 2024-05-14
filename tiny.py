from lex import *

def main():
    """
    source = "LET foobar = 123"
    lexer = Lexer(source)

    while lexer.peek() != '\0':
        print(lexer.curChar)
        lexer.nextChar()
    """
    #source = "+- */>>= = !="
    #source = "+ =#This is a comment!\n */"
    #source = "+- \"This is a string\" # This is a comment!\n */"
    source = "+-123 9.8654*/"
    lexer = Lexer(source)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token.kind)
        token = lexer.getToken()


main()
