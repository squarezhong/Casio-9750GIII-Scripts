import math

yaw = math.radians(float(input('yaw=')))
pitch = math.radians(float(input('pitch=')))
roll = math.radians(float(input('roll=')))

cr = math.cos(roll * 0.5)
sr = math.sin(roll * 0.5)
cp = math.cos(pitch * 0.5)
sp = math.sin(pitch * 0.5)
cy = math.cos(yaw * 0.5)
sy = math.sin(yaw * 0.5)

target = int(input('target 0=a, 1=e, 2=r, 3=q:'))

if target == 0 or target == 3:
    # convert euler angles (body zyx) to angle-axis
    # convert to quaternion first
    s = cr * cp * cy + sr * sp * sy
    x = sr * cp * cy - cr * sp * sy
    y = cr * sp * cy + sr * cp * sy
    z = cr * cp * sy - sr * sp * cy
    
    if target == 0:
        angle = 2 * math.acos(s)
        axis = (x / math.sqrt(1 - s * s),
                y / math.sqrt(1 - s * s),
                z / math.sqrt(1 - s * s))
    
        print('angle=', round(math.degrees(angle), 3))
        print('axis=', round(axis[0], 3), round(axis[1], 3), round(axis[2], 3))
    else:
        print('q=', round(s, 3), round(x, 3), round(y, 3), round(z, 3))
    
elif target == 1:
    print('no conversion needed')
elif target == 2:
    # convert euler angles (zyx) to rotation matrix
    r1 = [cp * cy, -cr * sy + sr * sp * cy, sr * sy + cr * sp * cy]
    r2 = [cp * sy, cr * cy + sr * sp * sy, -sr * cy + cr * sp * sy]
    r3 = [-sp, sr * cp, cr * cp]

    # print rotation matrix
    print('row1=', round(r1[0], 3), round(r1[1], 3), round(r1[2], 3))
    print('row2=', round(r2[0], 3), round(r2[1], 3), round(r2[2], 3))
    print('row3=', round(r3[0], 3), round(r3[1], 3), round(r3[2], 3))
else:
    print('invalid target')