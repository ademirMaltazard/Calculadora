from PyQt5 import uic, QtWidgets
from calculator import calculadora

#----------- EXECUÇÃO DAS FUNÇOES ------------

lastNumber = 0
operator = ''
changed = False

def Result(newOperator):
    global changed
    global lastNumber
    global operator
    print('antes ', operator)
    if operator == '':
        lastNumber = float(windown.label_numWindow.text())
        windown.label_numWindow.setText('')
        operator = newOperator
    else:
        operator = newOperator
        currentNumber = float(windown.label_numWindow.text())
        result = 0
        if operator == '+':
            result = calculadora.Sum(lastNumber, currentNumber)
        elif operator == '-':
            result = calculadora.Subtraction(lastNumber, currentNumber)
        elif operator == '*':
            result = calculadora.Multiplication(lastNumber, currentNumber)
        elif operator == '/':
            result = calculadora.Division(lastNumber, currentNumber)
        print(f'{result:.2f}')
        windown.label_numWindow.setText(f'{result:.2f}')
        lastNumber = float(result)
        print('depois ', operator)

def sumButton():
    global changed
    newOperator = windown.pushButton_plus.text()
    changed = True
    Result(newOperator)

def subtrationButton():
    newOperator = windown.pushButton_sub.text()
    Result(newOperator)

def multiplicationButton():
    newOperator = windown.pushButton_mult.text()
    Result(newOperator)

def divisionButton():
    newOperator = windown.pushButton_div.text()
    Result(newOperator)

# -------- COMANDOS PARA EXIBIÇÃO NA TELA ---------------
def addNumber1():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_1.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber2():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_2.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber3():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_3.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber4():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_4.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber5():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_5.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber6():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_6.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber7():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_7.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber8():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_8.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber9():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_9.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber0():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_0.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addDot():
    global changed
    if changed:
        windown.label_numWindow.setText('')
        changed = False
    num = windown.pushButton_dot.text()
    label = windown.label_numWindow.text()
    for i in label:
        if i == '.':
            return
    windown.label_numWindow.setText(label + num)


#----------- LOAD PAGES ----------

app = QtWidgets.QApplication([])

windown = uic.loadUi('windown.ui')

#---------- AÇÕES ---------
# === FUNCTIONS BUTTONS ===
windown.pushButton_plus.clicked.connect(sumButton)
windown.pushButton_sub.clicked.connect(subtrationButton)
windown.pushButton_mult.clicked.connect(multiplicationButton)
windown.pushButton_div.clicked.connect(divisionButton)

# === VALUES BUTTONS ====
windown.pushButton_0.clicked.connect(addNumber0)
windown.pushButton_1.clicked.connect(addNumber1)
windown.pushButton_2.clicked.connect(addNumber2)
windown.pushButton_3.clicked.connect(addNumber3)
windown.pushButton_4.clicked.connect(addNumber4)
windown.pushButton_5.clicked.connect(addNumber5)
windown.pushButton_6.clicked.connect(addNumber6)
windown.pushButton_7.clicked.connect(addNumber7)
windown.pushButton_8.clicked.connect(addNumber8)
windown.pushButton_9.clicked.connect(addNumber9)
windown.pushButton_dot.clicked.connect(addDot)


windown.show()
app.exec()
