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
        Addition(self, other)   #* TODO (použijte Addition)
        pass
    
    def __sub__(self, other):
        Addition(self, Multiplication(other, cst(-1))) #* TODO (použijte Addition a Multiplication se zápornou konstantu)
        pass
    
    def __mul__(self, other):
        Multiplication(self, other)  #* TODO (použijte Multiplication)
        pass
    
class BinaryOperator(Operator):
    def __init__(self, levy_argument, pravy_argument):
        self.levy_argument = levy_argument
        self.pravy_argument = pravy_argument
        
class UnaryOperator(Operator):
    def __init__(self, argument):
        self.argument = argument
    
    def __str__(self):
        return type(self).__name__ + "(" + str(self.argument) + ")"
        
class Addition(BinaryOperator):
    def __str__(self):
        print(self.levy_argument + self.pravy_argument) #* TODO vypíšeme něco jako (levy_argument)+(pravy_argument)
        pass
    def diff(self):
        Addition(identity(self.levy_argument), identity(self.pravy_argument)) #* TODO)
        pass
    
class Multiplication(BinaryOperator):
    def __str__(self):
        self.levy_argument * self.pravy_argument #* TODO vypíšeme něco jako (levy_argument)*(pravy_argument)
        pass
    def diff(self):
        Addition(Multiplication(identity(self.levy_argument), self.pravy_argument),Multiplication(self.levy_argument, identity(self.pravy_argument)))  #* TODO
        pass
    
class cst(UnaryOperator):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        print(self.value) #* TODO vypíšeme něco jako value
        pass
    def diff(self):
        print(0) #* TODO
        pass
    
class identity(UnaryOperator):
    def __init__(self):
        pass
    def __str__(self):
        print(x)  #* TODO vypíšeme něco jako x   
        pass
    def diff(self):
        print(1) #* TODO
        pass
    
class mocnina(UnaryOperator):
    def __init__(self, argument, exponent):
        self.argument = argument
        self.exponent = exponent
    def __str__(self):
        print(self.argument ** self.exponent)    #* TODO vypíšeme něco jako argument^exponent
        pass
    def diff(self):
        mocnina(self, self.exponent * self.argument, self.exponent -1)    #* TODO
        pass
    
class sin(UnaryOperator):
    def diff(self):
        print(cos)    #* TODO
        pass

class cos(UnaryOperator):
    def diff(self):
        print(-sin)   #* TODO
        pass

class exp(UnaryOperator):
    def diff(self):
        mocnina.diff(self)    #* TODO
        pass
    
class ln(UnaryOperator):
    def diff(self):
        1 // identity(self)    #* TODO
        pass

class frc(UnaryOperator):
    def __str__(self):
        print(1//mocnina.diff(self, -1))  #* TODO vypíšeme něco jako 1/(argument)
        pass
    
    def diff(self):
        self * self.diff(self)    #* TODO
        pass

# takto by se to mělo používat
x = identity()
# sin(x + cos(x*x)) + 1
f1 = sin(x + cos(x*x)) + cst(1)
print(f1)
print(f1.diff())