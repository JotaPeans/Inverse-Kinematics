import math


def forward_L(point_to:list, rotation_angle:int, rotations=False, arm_size=20, final_arm_size=10):
    '''returns the angles of rotations\n
    arm_size in centimeters'''

    x = point_to[0]
    y = point_to[1]
    z = point_to[2]

    if rotations == False:
        if x == (-1)*(y) or y == (-1)*(x) or x == y:
            x -= 10.13 # 7.07 + 3.06 -> 7.07 é a medida dos catetos que forma com a hipotenusa no valor do final do braço e 3.06 é a medida dos catetos que forma com a hipotenusa no valor 4.33 que é o tamanho do cateto da base do triangulo que forma com hipotenusa 5, parte da base.
            y -= 10.13 # 7.07 + 3.06 -> 7.07 é a medida dos catetos que forma com a hipotenusa no valor do final do braço e 3.06 é a medida dos catetos que forma com a hipotenusa no valor 4.33 que é o tamanho do cateto da base do triangulo que forma com hipotenusa 5, parte da base.
            z -= 2.5

        elif x == 0 and y != 0:
            y -= 14.33 # 10 que é o tamanho do final do braço e 4.33 que é o tamanho do cateto da base do triangulo que forma com hipotenusa 5, parte da base.
            z -= 2.5 # tamanho do cateto da altura do triangulo que forma com hipotenusa 5, parte da base.

        elif y == 0 and x != 0:
            x -= 14.33 # 10 que é o tamanho do final do braço e 4.33 que é o tamanho do cateto da base do triangulo que forma com hipotenusa 5, parte da base.
            z -= 2.5 # tamanho do cateto da altura do triangulo que forma com hipotenusa 5, parte da base.

        else:      # ↱ tamanho da ultima fase do braço                                                                  # ↱ transformando o paramentro de radianos para graus da função cos e sin
            x -= ( (final_arm_size * math.cos(rotation_angle * (math.pi/180))) + (4.33 * math.cos(rotation_angle * (math.pi/180))))
            y -= ( (final_arm_size * math.sin(rotation_angle * (math.pi/180))) + (4.33 * math.sin(rotation_angle * (math.pi/180))))
            z -= 2.5


    L = math.sqrt((x*x) + (y*y))

    h = math.sqrt((L*L) + (z*z))

    if h > 40:
        print('a coordenada nao pode ser alcancada !')
        return None

    try:

        phi = math.atan(z / L) * (180 / math.pi)  # -> degrees

        theta = math.acos((h / 2) / arm_size) * (180 / math.pi)  # -> degrees

        a1 = math.ceil(phi + theta)
        a2 = math.ceil(phi - theta)

        if a2 > 0:
            a3 = a2 - a2
        elif a2 < 0:
            a3 = -(a2) + a2
        elif a2 == 0:
            a3 = 0
            
        return a1, a2, a3

    except:
        print('\na coordenada nao pode ser alcancada\n')
        return None


if __name__ == "__main__":
    pass