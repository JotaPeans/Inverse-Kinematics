import math
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import forward
import sys
from PyQt6 import uic, QtWidgets


class Window ():
    def __init__(self, point_to=[0, 22, 6, 0, 0, 0], arm_size=20, final_arm_size=10) -> None:
        '''### point_to -> [ x, y, z, rx, ry, rz ]'''

    #Janela:
        self.form = uic.loadUi('Ui/Robotic Arm v2.ui')

        #self.form.run_ik.clicked.connect(self.getValues)
        self.form.reset.clicked.connect(self.resetValues)

        self.form.X_axis.valueChanged.connect(self.valueX)
        self.form.Y_axis.valueChanged.connect(self.valueY)
        self.form.Z_axis.valueChanged.connect(self.valueZ)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.form.Box_figure.addWidget(self.canvas)
        #self.form.Box_figure.removeWidget(self.canvas)

        self.form.show()
        

    #Arm:
        if len(point_to) <= 3:
            for x in range(3):
                point_to.append(0)

        self.arm_size = arm_size
        self.final_arm_size = final_arm_size

        self.r = 90

        self.a1 = 0
        self.a2 = 0
        self.a3 = 0

        self.point_to = point_to[0:3]

        self.rx = point_to[3]
        self.ry = point_to[4]
        self.rz = point_to[5]

        self.form.X_axis.setValue(int(self.point_to[0]))
        self.form.Y_axis.setValue(int(self.point_to[1]))
        self.form.Z_axis.setValue(int(self.point_to[2]))

        self.calculate()


    #def getValues(self):
    #    X_value = self.form.X_axis.value()
    #    Y_value = self.form.Y_axis.value()
    #    Z_value = self.form.Z_axis.value()
    #
    #    self.point_to = [X_value, Y_value, Z_value, 0, 0, 0]
    #    self.calculate()

    def valueX(self, value):
        self.form.point_X.setText(str(value))
        self.point_to[0] = float(value)
        self.calculate()

    def valueY(self, value):
        self.form.point_Y.setText(str(value))
        self.point_to[1] = float(value)
        self.calculate()

    def valueZ(self, value):
        self.form.point_Z.setText(str(value))
        self.point_to[2] = float(value)
        self.calculate()

    def resetValues(self):
        self.point_to = [0, 22, 6, 0, 0, 0]
        self.form.X_axis.setValue(int(self.point_to[0]))
        self.form.Y_axis.setValue(int(self.point_to[1]))
        self.form.Z_axis.setValue(int(self.point_to[2]))
        self.calculate()

    def calculate(self):
        try:
            #self.Length = math.sqrt((self.point_to[0]**2) + (self.point_to[1]**2))

            self.r, self.a1, self.a2, self.a3 = forward.rotations(point_to=self.point_to, ry=self.ry, rx=self.rx, rz=self.rz)

            #self.a1, self.a2, self.a3 = forward.calculate_motor_angles(a1 = self.a1, a2 = self.a2, ry = self.ry)

            #print(f'rotation = {self.r}')
            #print(f'a1 = {self.a1}')
            #print(f'a2 = {self.a2}')
            #print(f'a3 = {self.a3}')
            #print()

            self.plot_forward_view()

        except:
            print('A coordenada nao pode ser alcancada !')

    def plot_forward_view(self):
        self.figure.clear()

        x = [0]
        y = [0]
        z = [0, 2.5]

        # Coloca no vetor x e y a posição relativa do proximo ponto
        x.append((5 * math.cos(30 * (math.pi/180))) * math.cos(self.r * (math.pi/180)))
        y.append((5 * math.cos(30 * (math.pi/180))) * math.sin(self.r * (math.pi/180)))

        x1 = x[1] + (self.arm_size * math.cos(self.a1 * (math.pi/180))) * (math.cos(self.r * (math.pi/180)))
        y1 = y[1] + (self.arm_size * math.cos(self.a1 * (math.pi/180))) * (math.sin(self.r * (math.pi/180)))
        z1 = z[1] + self.arm_size * (math.sin(self.a1 * (math.pi/180)))

        x.append(x1)
        y.append(y1)
        z.append(z1)

        x2 = x1 + (self.arm_size * math.cos(self.a2 * (math.pi/180))) * (math.cos(self.r * (math.pi/180)))
        y2 = y1 + (self.arm_size * math.cos(self.a2 * (math.pi/180))) * (math.sin(self.r * (math.pi/180)))
        z2 = z1 + self.arm_size * (math.sin(self.a2 * (math.pi/180)))

        x.append(x2)
        y.append(y2)
        z.append(z2)

        x3 = x2 + (self.final_arm_size * math.cos(self.a3 * (math.pi/180))) * (math.cos(self.r * (math.pi/180)))
        y3 = y2 + (self.final_arm_size * math.cos(self.a3 * (math.pi/180))) * (math.sin(self.r * (math.pi/180)))
        z3 = z2 + self.final_arm_size * (math.sin(self.a3 * (math.pi/180)))

        x.append(x3)
        y.append(y3)
        z.append(z3)

        ax = plt.axes(projection='3d')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_xlim([-60, 60])
        ax.set_ylim([-60, 60])
        ax.set_zlim([0, 50])

        ax.plot(x[0:2], y[0:2], z[0:2], color='orange', marker='o', linestyle='solid', linewidth=2, markersize=5)  # base
        ax.plot(x[1:3], y[1:3], z[1:3], color='red', marker='o', linestyle='solid', linewidth=2, markersize=5)  # arm_1
        ax.plot(x[2:4], y[2:4], z[2:4], color='blue', marker='o', linestyle='solid', linewidth=2, markersize=5)  # arm_2
        ax.plot(x[3:5], y[3:5], z[3:5], color='green', marker='o', linestyle='solid', linewidth=2, markersize=5)  # arm_3 -> final_arm


        self.canvas.draw()

        #plt.show()



app = QtWidgets.QApplication([])
#j = Window(point_to=[0, 50, 15, 0, 0, 0])
j = Window()
sys.exit(app.exec())