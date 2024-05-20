import math

s, x, y, z = map(float, input('q=').split())

target = int(input('target 0=a, 1=e, 2=r, 3=q:'))

if target == 0:
    angle = 2 * math.acos(s)
    axis = (x / math.sqrt(1 - s * s),
            y / math.sqrt(1 - s * s),
            z / math.sqrt(1 - s * s))

    print('angle=', round(math.degrees(angle), 3))
    print('axis=', round(axis[0], 3), round(axis[1], 3), round(axis[2], 3))
elif target == 1:
    # transform quaternion to euler angles (body zyx)
    # quaternion should be normalized
    # https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles
    row = math.atan2(2 * (s * x + y * z), 1 - 2 * (x * x + y * y))
    pitch = math.asin(2 * (s * y - z * x))
    yaw = math.atan2(2 * (s * z + x * y), 1 - 2 * (y * y + z * z))

    # print euler angles
    print('body z-y-x')
    print('yaw=', round(math.degrees(yaw), 3))
    print('pitch=', round(math.degrees(pitch), 3))
    print('roll=', round(math.degrees(row), 3))
elif target == 2:
    # transform quaternion to rotation matrix
    r11 = 1 - 2 * (y * y + z * z)
    r12 = 2 * (x * y - s * z)
    r13 = 2 * (x * z + s * y)
    r21 = 2 * (x * y + s * z)
    r22 = 1 - 2 * (x * x + z * z)
    r23 = 2 * (y * z - s * x)
    r31 = 2 * (x * z - s * y)
    r32 = 2 * (y * z + s * x)
    r33 = 1 - 2 * (x * x + y * y)

    # print rotation matrix
    print('rotation matrix:')
    print(round(r11, 3), round(r12, 3), round(r13, 3))
    print(round(r21, 3), round(r22, 3), round(r23, 3))
    print(round(r31, 3), round(r32, 3), round(r33, 3))
elif target == 3:
    print('no conversion needed')
else:
    print('invalid target')