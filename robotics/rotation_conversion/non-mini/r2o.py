import math

r11, r12, r13 = map(float, input('row1=').split())
r21, r22, r23 = map(float, input('row2=').split())
r31, r32, r33 = map(float, input('row3=').split())

target = int(input('target 0=a, 1=e, 2=r, 3=q:'))

if target == 0:
    # convert rotation matrix to angle-axis
    # https://www.euclideanspace.com/maths/geometry/rotations/conversions/matrixToAngle/

    # calculate angle
    angle = math.acos((r11 + r22 + r33 - 1) / 2)
    x = (r32 - r23) / math.sqrt((r32 - r23) ** 2 + (r13 - r31) ** 2 + (r21 - r12) ** 2)
    y = (r13 - r31) / math.sqrt((r32 - r23) ** 2 + (r13 - r31) ** 2 + (r21 - r12) ** 2)
    z = (r21 - r12) / math.sqrt((r32 - r23) ** 2 + (r13 - r31) ** 2 + (r21 - r12) ** 2)
    
    # print angle-axis
    print('angle=', round(math.degrees(angle), 3))
    print('axis=', round(x, 3), round(y, 3), round(z, 3))
elif target == 1:
    # convert rotation matrix to euler angles (body zyx)
    # calculate pitch
    pitch = -math.asin(r31)
    if pitch == math.pi / 2:
        roll = 0
        yaw = math.atan2(r12, r13)
    elif pitch == -math.pi / 2:
        roll = 0
        yaw = -math.atan2(r12, r13)
    else:
        roll = math.atan2(r32 / math.cos(pitch), r33 / math.cos(pitch))
        yaw = math.atan2(r21 / math.cos(pitch), r11 / math.cos(pitch))
        
    # print euler angles
    print('body z-y-x')
    print('yaw=', round(math.degrees(yaw), 3))
    print('pitch=', round(math.degrees(pitch), 3))
    print('roll=', round(math.degrees(roll), 3))

elif target == 2:
    print('no conversion needed')
elif target == 3:
    # transform rotation matrix to quaternion
    # https://en.m.wikipedia.org/wiki/Rotation_formalisms_in_three_dimensions#Conversion_formulae_between_formalisms
    s = math.sqrt(1 + r11 + r22 + r33) / 2
    x = (r32 - r23) / (4 * s)
    y = (r13 - r31) / (4 * s)
    z = (r21 - r12) / (4 * s)

    # print quaternion
    print('q=', round(s, 3), round(x, 3), round(y, 3), round(z, 3))
else:
    print('invalid target')