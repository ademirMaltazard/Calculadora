from PyQt5 import uic, QtWidgets
from calculator import calculadora

#----------- EXECUÇÃO DAS FUNÇOES ------------

lastNumber = 0
currentNumber = 20

def sumButton():

    result = calculadora.Sum(lastNumber, currentNumber)
    windown.label_numWindow.setText(str(result))


# -------- COMANDOS PARA EXIBIÇÃO NA TELA ---------------
def addNumber1():
    num = windown.pushButton_1.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber2():
    num = windown.pushButton_2.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber3():
    num = windown.pushButton_3.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber4():
    num = windown.pushButton_4.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber5():
    num = windown.pushButton_5.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber6():
    num = windown.pushButton_6.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber7():
    num = windown.pushButton_7.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber8():
    num = windown.pushButton_8.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber9():
    num = windown.pushButton_9.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addNumber0():
    num = windown.pushButton_0.text()
    label = windown.label_numWindow.text()
    windown.label_numWindow.setText(label + num)

def addDot():
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
