class Num:
    def __init__(self, value):
        self.value = value

    def __int__(self):
        return self.value


class Add(Num):
    def __init__(self, *args):
        self.operands = args
        super().__init__(sum(int(arg) for arg in args))


class Mul(Num):
    def __init__(self, *args):
        self.operands = args
        total = 1
        for arg in self.operands:
            total *= int(arg)
        super().__init__(total)


class PrintVisitor:
    def __init__(self):
        pass

    def visit(self, num: Num):
        if type(num) is Num or len(num.operands) <= 1:
            return str(int(num))

        expr = f"({self.visit(num.operands[0])}"
        for op in range(1, len(num.operands)):
            expr += " + " * (type(num) is Add)
            expr += " * " * (type(num) is Mul)
            expr += f"{self.visit(num.operands[op])}"
        expr += ")"
        return expr


class CalcVisitor:
    def __init__(self):
        pass

    def visit(self, num: Num):
        return int(num)


class StackVisitor:
    def __init__(self):
        pass

    def visit(self, num: Num):
        if type(num) is Num or len(num.operands) <= 1:
            return "PUSH " + str(int(num)) + '\n'

        expr = ""
        for op in range(len(num.operands)):
            expr += self.visit(num.operands[op])
        expr += "MUL\n" * (type(num) is Mul)
        expr += "ADD\n" * (type(num) is Add)
        return expr


ast = Add(Num(7), Mul(Num(3), Num(2)))

pv = PrintVisitor()
print(pv.visit(ast))

cv = CalcVisitor()
print(cv.visit(ast))

sv = StackVisitor()
print(sv.visit(ast))
