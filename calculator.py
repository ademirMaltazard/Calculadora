
class calculator():
    def __init__(self):
        self.memory = 0
        self.lastValor = 0
    
    def Sum(self, firstNumber, secondNumber):
        operation = firstNumber + secondNumber
        self.lastValor = operation
        return operation

    def Subtraction(self,  firstNumber, secondNumber):
        operation = firstNumber - secondNumber
        self.lastValor = operation
        return operation

    def Division(self,  firstNumber, secondNumber):
        if secondNumber != 0:
            operation = firstNumber / secondNumber
            self.lastValor = operation
            return operation
        else:
            return (f'Operação invalida!!!')

    def Multiplication(self,  firstNumber, secondNumber):
        operation = firstNumber * secondNumber
        self.lastValor = operation
        return operation
    
    def CheckMemory(self):
        return (f'Memoria: {self.memory}')

    def AddValorToMemory(self):
        self.memory += self.lastValor
    
    def SubtractValorToMemory(self):
        self.memory -= self.lastValor
    
    def CleanMemory(self):
        self.memory = 0

calculadora = calculator()
'''
print("soma: ",calculadora.Sum(15, 20))
calculadora.AddValorToMemory()
print(1, calculadora.CheckMemory())
print("sub:", calculadora.Subtraction(20, 2))
print(2, calculadora.CheckMemory())
calculadora.SubtractValorToMemory()
print(3, calculadora.CheckMemory())
calculadora.CleanMemory()
print(4, calculadora.CheckMemory())
'''