from PyQt6 import uic, QtWidgets

def principal():
    print('botão clicado')

app = QtWidgets.QApplication([])
form = uic.loadUi('Ui/Robotic Arm.ui')

#form.run_ik.clicked.connect(principal)
#form.run_ik.setStyleSheet('QPushButton {border: None; border-radius:10px; background-color:#729B79; } QPushButton:hover {background-color:#668F6D;}')

form.show()

app.exec()