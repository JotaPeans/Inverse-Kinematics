import math
import forward


class Arm():
    def __init__(self, point_to=[0, 21.4, 5.43, 0, 0, 0], rotation_angle=90, a1=90, a2=0, a3=-45) -> None:
        '''## default_first_point -> [ x, y, z, rx, ry, rz ]'''
 
        if len(point_to) <= 3:
            for x in range(3):
                point_to.append(0)

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

            self.r, self.a1, self.a2, self.a3 = forward.rotations(point_to = self.point_to, ry = self.ry, rx = self.rx, rz = self.rz, rotation_angle = self.r)

            #self.a1, self.a2, self.a3 - forward.calculate_motor_angles(a1 = self.a1, a2 = self.a2, ry = self.ry)

            print(f'rotation = {self.r}')
            print(f'a1 = {self.a1}')
            print(f'a2 = {self.a2}')
            print(f'a3 = {self.a3}')
            print()

        except:
            print('erro')


Arm(point_to=[20, 10, 15])
