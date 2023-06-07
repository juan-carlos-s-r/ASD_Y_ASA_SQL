class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0

    def parse(self):
        self.Q()

    def igualar(self, token_esperado):
        if self.index < len(self.tokens) and self.tokens[self.index] == token_esperado:
            self.index += 1
        else:
            print(f"Error de sintaxis. Se esperaba {token_esperado}, se encontró {self.tokens[self.index]}")

    def Q(self):
        self.igualar("select")
        self.D()
        self.igualar("from")
        self.T()

    def D(self):
        if self.index < len(self.tokens) and self.tokens[self.index] == "distinct":
            self.igualar("distinct")
            self.P()
        else:
            self.P()

    def P(self):
        if self.index < len(self.tokens) and self.tokens[self.index] == "*":
            self.igualar("*")
        elif self.index < len(self.tokens) and self.tokens[self.index].isidentifier():
            self.A()
        else:
            print(f"Error de sintaxis. Se esperaba '*' o un identificador, se encontró {self.tokens[self.index]}")

    def A(self):
        self.A2()
        self.A1()

    def A1(self):
        if self.index < len(self.tokens) and self.tokens[self.index] == ",":
            self.igualar(",")
            self.A()
        else:
            pass

    def A2(self):
        self.igualar(self.tokens[self.index])

    def T(self):
        self.T2()
        self.T1()

    def T1(self):
        if self.index < len(self.tokens) and self.tokens[self.index] == ",":
            self.igualar(",")
            self.T()
        else:
            pass

    def T2(self):
        self.igualar(self.tokens[self.index])


while(True):
    token=input(str(">>>"))
    tokens=token.split()
    if token=="cerrar":
        break
    else:
        
        parser = Parser(tokens)
        parser.parse()
        print("Análisis sintáctico exitoso.")
        token=""
        tokens.remove