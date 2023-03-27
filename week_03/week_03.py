class Operator:
    def __init__(self):
        pass
    
    def __str__(self):
        return type(self).__name__
    
    def __repr__(self):
        return self.__str__()
    
    def diff(self):
        pass
    
    def __add__(self, other):
        return Addition(self, other)

    def __sub__(self, other):
        return Addition(self, Multiplication(cst(-1), other))
    
    def __mul__(self, other):
        return Multiplication(self, other)
    
class BinaryOperator(Operator):
    def __init__(self, levy_argument, pravy_argument):
        self.levy_argument = levy_argument
        self.pravy_argument = pravy_argument

    def __str__(self):
        return "(" + str(self.levy_argument) + " " + type(self).__name__ + " " + str(self.pravy_argument) + ")"
        
class UnaryOperator(Operator):
    def __init__(self, argument):
        self.argument = argument
    
    def __str__(self):
        return type(self).__name__ + "(" + str(self.argument) + ")"
        
class Addition(BinaryOperator):
    def __str__(self):
        return "(" + str(self.levy_argument) +  "+" + str(self.pravy_argument) + ")"
    def diff(self):
        return self.levy_argument.diff() + self.pravy_argument.diff()
    
class Multiplication(BinaryOperator):
    def __str__(self):
        return "(" + str(self.levy_argument) + "*" + str(self.pravy_argument) + ")"
    def diff(self):
        return self.levy_argument.diff() * self.pravy_argument + self.levy_argument * self.pravy_argument.diff() 

    
class cst(UnaryOperator):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value)
    def diff(self):
        return cst(0)
    
class identity(UnaryOperator):
    def __init__(self):
        pass
    def __str__(self):
        return "x"
    def diff(self):
        return cst(1)
    
class mocnina(UnaryOperator):
    def __init__(self, argument, exponent):
        self.argument = argument
        self.exponent = exponent

    def __str__(self):
        return "(" + str(self.argument) + ")^" + str(self.exponent)
    
    def diff(self):
        return Multiplication(self.exponent, mocnina(self.argument, self.exponent - 1) * self.argument.diff())
    
class sin(UnaryOperator):
    def __init__(self,argument):
        self.argument = argument

    def __str__(self):
        return "sin(" + str(self.argument) + ")"
    
    def diff(self):
        return cos(self.argument) * self.argument.diff()

class cos(UnaryOperator):
    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "cos(" + str(self.argument) + ")"
    
    def diff(self):
        return Multiplication(sin(self.argument), self.argument.diff() * cst(-1))

class exp(UnaryOperator):
    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "exp(" + str(self.argument) + ")"

    def diff(self):
        return Multiplication(exp(self.argument), self.argument.diff())
    
class ln(UnaryOperator):
    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "ln(" + str(self.argument) + ")"

    def diff(self):
        return Multiplication(frc(identity(), self.argument), self.argument.diff())

class frc(UnaryOperator):
    def __init__(self, argument):
        self.argument = argument
    
    def __str__(self):
        return "1/(" + str(self.argument) + ")"
    
    def diff(self):
        return Multiplication(cst(-1), frc(mocnina(self.argument, 2)) * self.argument.diff())
    


x = identity()
f1 = sin(x + cos(x*x)) + cst(1)
print(f1)
print(f1.diff())