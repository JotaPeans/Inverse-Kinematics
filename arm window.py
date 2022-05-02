from ast import For
from tkinter import *
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import forward


janela = Tk()


class Arm():                                                              #  x    y    z    rx ry rz
    def __init__(self, root, r=90, a1=90, a2=0, a3=-45, default_first_point=[0, 21.4, 5.43, 0, 0, 0]) -> None:
        self.r = r  # rotaciona o arm para 90 graus _|_

        self.a1 = a1  # angulo patradao da posição de inicio
        self.a2 = a2  # angulo patradao da posição de inicio
        self.a3 = a3  # angulo patradao da posição de inicio
        
        self.point_to = default_first_point[0:3]  # posição padrao de inicio

        self.rx = default_first_point[3] # angulo de rotação patradao da posição de inicio
        self.ry = default_first_point[4] # angulo de rotação patradao da posição de inicio
        self.rz = default_first_point[5] # angulo de rotação patradao da posição de inicio


        self.root = root
        self.root.title('Robotic arm')
        self.root.geometry('480x700')
        self.root.resizable(False, False)

        self.label_X = Label(text='X', font=('Arial', 10))
        self.label_X.grid(row=5, column=5)
        self.slide_X = Scale(self.root, from_=-40, to=40, resolution=0.5, orient=HORIZONTAL, command=self.value_X, length=300)  # X Axis
        self.slide_X.grid(row=6, column=5)

        self.label_Y = Label(text='Y', font=('Arial', 10))
        self.label_Y.grid(row=7, column=5)
        self.slide_Y = Scale(self.root, from_=0, to=60, resolution=0.5, orient=HORIZONTAL, command=self.value_Y, length=300)  # Y Axis
        self.slide_Y.grid(row=8, column=5)

        self.label_Z = Label(text='Z', font=('Arial', 10))
        self.label_Z.grid(row=9, column=5)
        self.slide_Z = Scale(self.root, from_=0, to=50, resolution=0.5, orient=HORIZONTAL, command=self.value_Z, length=300)  # Z Axis
        self.slide_Z.grid(row=10, column=5)

        self.root.mainloop()

    def value_X(self, X):
        self.point_to[0] = float(X)
        print(self.point_to)
        self.calculate()

    def value_Y(self, Y):
        self.point_to[1] = float(Y)
        print(self.point_to)
        self.calculate()

    def value_Z(self, Z):
        self.point_to[2] = float(Z)
        print(self.point_to)
        self.calculate()

    def calculate(self):
        try:
            self.Length = math.sqrt((self.point_to[0]**2) + (self.point_to[1]**2))
            self.r = math.atan2(self.point_to[1], self.point_to[0]) * (180/math.pi)

            self.a1, self.a2, self.a3 = forward.rotations(point_to = self.point_to, ry = self.ry, rx = self.rx, rz = self.rz, rotation_angle = self.r)

            #print(f'L = {self.Length}')
            #print(f'rotation = {self.r}')
            print(f'a1 = {self.a1}')
            print(f'a2 = {self.a2}')
            print(f'a3 = {self.a3}')
            print()

            self.plot_forward_view()

        except:
            pass

    def plot_rotation_view(self):
        x = [0, self.point_to[0]]
        y = [0, self.point_to[1]]

        figure = plt.figure(figsize=(8, 8), dpi=60)
        figure.add_subplot(111).plot(x, y)

        canvas = FigureCanvasTkAgg(figure, self.root)
        canvas.get_tk_widget().grid(row=12, column=5)

    def plot_forward_view(self):

        j1_x = 20 * (math.cos(self.a1 * (math.pi/180)))
        j1_y = 20 * (math.sin(self.a1 * (math.pi/180)))
        
        j2_x = 20 * (math.cos(self.a2 * (math.pi/180))) + j1_x
        j2_y = 20 * (math.sin(self.a2 * (math.pi/180))) + j1_y

        j3_x = j2_x + 10
        j3_y = j2_y

        x = [0, 4.33, j1_x, j2_x, j3_x]
        y = [0, 2.5, j1_y, j2_y, j3_y]

        figure = plt.figure(figsize=(8, 8), dpi=60)
        figure.add_subplot(111).plot(x, y)

        canvas = FigureCanvasTkAgg(figure, self.root)
        canvas.get_tk_widget().grid(row=12, column=5)


Arm(root=janela)
