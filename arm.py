import math
import forward


class Arm():
    def __init__(self, r=90, a1=90, a2=0, a3=-45, default_first_point=[0, 21.4, 5.43], default_rotations=[0, 0, 0]) -> None:
        self.r = r  # rotaciona o arm para 90 graus _|_
        self.a1 = a1  # angulo patradao da posição de inicio
        self.a2 = a2  # angulo patradao da posição de inicio
        self.a3 = a3  # angulo patradao da posição de inicio
        self.point_to = default_first_point  # posição padrao de inicio
        self.calculate()


    def calculate(self):
        try:
            #calcula a rotação e o comprimento total para a coordenada desejada!
            self.Length = math.sqrt((self.point_to[0]**2) + (self.point_to[1]**2))
            self.r = math.atan2(self.point_to[1], self.point_to[0]) * (180/math.pi) #radians to degrees

            self.a1, self.a2, self.a3 = forward.forward_L(self.point_to, self.r)

            #self.a1, self.a2, self.a3 = forward.calculate_motor_angles(self.a1, self.a2)

            print(f'rotation = {self.r}')
            print(f'a1 = {self.a1}')
            print(f'a2 = {self.a2}')
            print(f'a3 = {self.a3}')
            print()

        except:
            print('\nInsira no formato: X Y Z -> ex: -20 25 10\n')
            self.calculate()


Arm(default_first_point=[20,10,15])
