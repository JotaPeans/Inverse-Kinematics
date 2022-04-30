import math
import time

# Deve ser função assíncrona


def motor_desaceleration(total_angle):
    '''makes the desaceleration for motor'''

    angle = 0
    while angle < total_angle - (total_angle / 50):
        divison = total_angle / 50
        angle += divison
        print(math.ceil(angle))  # faria o upload de cada angulo do motor

        if math.ceil(angle) < total_angle - 30:
            time.sleep(0.02)
        else:
            time.sleep(0.1)


if __name__ == '__main__':
    motor_desaceleration(29)
