import math
import matplotlib.pyplot as plt
import forward


class Arm():
    def __init__(self, point_to=[0, 21.4, 5.43, 0, 0, 0], arm_size=20, final_arm_size=10, rotation_angle=90, a1=90, a2=0, a3=-45) -> None:
        '''## default_first_point -> [ x, y, z, rx, ry, rz ]'''

        if len(point_to) <= 3:
            for x in range(3):
                point_to.append(0)

        self.arm_size = arm_size
        self.final_arm_size = final_arm_size

        self.r = rotation_angle

        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

        self.point_to = point_to[0:3]

        self.rx = point_to[3]
        self.ry = point_to[4]
        self.rz = point_to[5]

        self.calculate()

    def calculate(self):
        try:
            #self.Length = math.sqrt((self.point_to[0]**2) + (self.point_to[1]**2))

            self.r, self.a1, self.a2, self.a3 = forward.rotations(
                point_to=self.point_to, ry=self.ry, rx=self.rx, rz=self.rz)

            #self.a1, self.a2, self.a3 = forward.calculate_motor_angles(a1 = self.a1, a2 = self.a2, ry = self.ry)

            print(f'rotation = {self.r}')
            print(f'a1 = {self.a1}')
            print(f'a2 = {self.a2}')
            print(f'a3 = {self.a3}')
            print()

            self.plot_forward_view()

        except:
            print('Erro Inesperado')

    def plot_forward_view(self):
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
        ax.set_xlim([-40, 40])
        ax.set_ylim([0, 60])
        ax.set_zlim([0, 50])

        ax.plot(x[0:2], y[0:2], z[0:2], color='orange', marker='o', linestyle='solid', linewidth=2, markersize=5)  # base
        ax.plot(x[1:3], y[1:3], z[1:3], color='red', marker='o', linestyle='solid', linewidth=2, markersize=5)  # arm_1
        ax.plot(x[2:4], y[2:4], z[2:4], color='blue', marker='o', linestyle='solid', linewidth=2, markersize=5)  # arm_2
        ax.plot(x[3:5], y[3:5], z[3:5], color='green', marker='o', linestyle='solid', linewidth=2, markersize=5)  # arm_3 -> final_arm

        plt.show()


Arm(point_to=[0, 50, 10, 0, 0, 0])
