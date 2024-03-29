import math
import numpy as np


#calculo dos pontos que forma um circulo com o raio de tamanho = final_arm_size
R = 10 # final_arm_size -> raio do circulo
n = 360 # numero de arestas que formam o circulo

#calculo dos pontos
t = np.linspace(0, 2 * np.pi, n)
x_coordnates = R * np.cos(t) # coordenadas dos pontos do eixo x do circulo
y_coordnates = R * np.sin(t) # coordenadas dos pontos do eixo y do circulo


def forward_L(point_to:list, arm_size=20, final_arm_size=10):
    '''returns the angles of rotations\n
    arm_size in centimeters'''

    x = point_to[0]
    y = point_to[1]
    z = point_to[2]

    '''if rotations == False:
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
            z -= 2.5'''

    L = math.sqrt((x*x) + (y*y))

    h = math.sqrt((L*L) + (z*z))

    if h > 40:
        raise Exception()

    try:

        phi = math.atan(z / L) * (180 / math.pi)  # -> to degrees

        theta = math.acos((h / 2) / arm_size) * (180 / math.pi)  # -> to degrees

        a1 = math.ceil(phi + theta)
        a2 = math.ceil(phi - theta)
        a3 = 0

        #if a2 > 0:
        #    a3 = a2 - a2
        #elif a2 < 0:
        #    a3 = -(a2) + a2
        #elif a2 == 0:
        #    a3 = 0
            
        return a1, a2, a3

    except:
        print('\nA coordenada nao pode ser alcancada !\n')
        return None


def calculate_motor_angles(a1:int, a2:int, ry=0):
    a2T = ( a2 - ( a1-90 ) )
    a3T = 90 - a2

    if ry != 0:
        a3T = 180 - ( 90 + a2 + ry) 

    return a1, a2T, a3T


def rotations(point_to:list, ry:int, rx:int, rz:int, final_arm_size=10):
    x = point_to[0]
    y = point_to[1]
    z = point_to[2]

    #faz o calculo de rotação
    rotation_angle = int(math.atan2(y, x) * (180/math.pi))

    #faz o calculo das coordenadas da segunda rotação (ry)
    x -= x_coordnates[abs(ry)] * math.cos( rotation_angle * (math.pi/180) ) + (4.33 * math.cos( rotation_angle * (math.pi/180) ))
    y -= x_coordnates[abs(ry)] * math.sin( rotation_angle * (math.pi/180) ) + (4.33 * math.sin( rotation_angle * (math.pi/180) ))
    z += ( final_arm_size * math.sin(ry * (math.pi/180))) - 2.5

    #faz o calculo das coordenadas da primeira rotação (rx)
    x += y_coordnates[abs(rx)]
    y += ( R - x_coordnates[abs(rx)] )

    #atribui a rotação do eixo z a rotação (rz)
        #fazer


    a1, a2, a3 = forward_L(point_to=[x, y, z])
    
    return rotation_angle, a1, a2, a3


if __name__ == '__main__':
    a1, a2, a3 = rotations([20,10,15], 0, 0, 0)

    print('a1 =', a1)
    print('a2 =', a2)
    print('a3 =', a3)

