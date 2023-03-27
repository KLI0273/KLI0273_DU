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
        return Addition(self, other)   #* TODO (použijte Addition)
        pass

    def __sub__(self, other):
        return Addition(self, Multiplication(cst(-1), other)) #* TODO (použijte Addition a Multiplication se zápornou konstantu)
        pass
    
    def __mul__(self, other):
        return Multiplication(self, other)  #* TODO (použijte Multiplication)
        pass
    
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
#    def __str__(self):
#        return self.levy_argument.diff() + self.pravy_argument.diff() #* TODO vypíšeme něco jako (levy_argument)+(pravy_argument)
#        pass
    def diff(self):
        return self.levy_argument.diff() + self.pravy_argument.diff() #?Addition(identity(self.levy_argument), identity(self.pravy_argument)) #* TODO
        pass
    
class Multiplication(BinaryOperator):
#    def __str__(self):
#        self.levy_argument * self.pravy_argument #* TODO vypíšeme něco jako (levy_argument)*(pravy_argument)
#        pass
    def diff(self):
        return self.levy_argument.diff() * self.pravy_argument.diff() + self.levy_argument * self.pravy_argument.diff() #?Addition(Multiplication(identity(self.levy_argument), self.pravy_argument),Multiplication(self.levy_argument, identity(self.pravy_argument)))  #* TODO
        pass
    
class cst(UnaryOperator):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return str(self.value) #* TODO vypíšeme něco jako value
        pass
    def diff(self):
        return cst(0) #* TODO
        pass
    
class identity(UnaryOperator):
    def __init__(self):
        pass
    def __str__(self):
        return "x"    #?print(x)  #* TODO vypíšeme něco jako x   
        pass
    def diff(self):
        return cst(1) #* TODO
        pass
    
class mocnina(UnaryOperator):
    def __init__(self, argument, exponent):
        self.argument = argument
        self.exponent = exponent
    def __str__(self):
        return "(" + str(self.argument) + ")^" + str(self.exponent)    #* TODO vypíšeme něco jako argument^exponent
        pass
    def diff(self):
        return Multiplication(self.exponent, mocnina(self.argument, self.exponent - 1) * self.argument.diff()) #?mocnina(self, self.exponent * self.argument, self.exponent -1)    #* TODO
        pass
    
class sin(UnaryOperator):
    def __init__(self,argument):
        self.argument = argument

    def __str__(self):
        return "sin(" + str(self.argument) + ")"
    
    def diff(self):
        return cos(self.argument) * self.argument.diff() #?print(cos)    #* TODO
        pass

class cos(UnaryOperator):
    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "cos(" + str(self.argument) + ")"
    
    def diff(self):
        return Multiplication(sin(self.argument) * self.argument.diff(), -1)  #?print(-sin)   #* TODO
        pass

class exp(UnaryOperator):
    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "exp(" + str(self.argument) + ")"

    def diff(self):
        return Multiplication(exp(self.argument), self.argument.diff())        #?mocnina.diff(self)    #* TODO
        pass
    
class ln(UnaryOperator):
    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "ln(" + str(self.argument) + ")"

    def diff(self):
        return Multiplication(frc(identity(), self.argument), self.argument.diff())
        #?1 // identity(self)    #* TODO
        pass

class frc(UnaryOperator):
    def __init__(self, argument):
        self.argument = argument

    def __str__(self):
        return "1/(" + str(self.argument) + ")"    #? print(1//mocnina.diff(self, -1))  #* TODO vypíšeme něco jako 1/(argument)
        pass
    
    def diff(self):
        return Multiplication(cst(-1), Multiplication(Multiplication(self.argument.diff(), self), Multiplication(self.argument, self)))    #? self * self.diff(self)    #* TODO
        pass

# takto by se to mělo používat
x = identity()
# sin(x + cos(x*x)) + 1
f1 = sin(x + cos(x*x)) + cst(1)
print(f1)
print(f1.diff())