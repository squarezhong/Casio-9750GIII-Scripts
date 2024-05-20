import math
angle=float(input('angle='))
angle=math.radians(angle)
x,y,z=map(float,input('axis(xyz)=').split())
target=int(input('target 0=a, 1=e, 2=r, 3=q:'))
if target==0:print('no conversion needed')
elif target==1 or target==3:
	s1=math.cos(angle/2);x1=x*math.sin(angle/2);y1=y*math.sin(angle/2);z1=z*math.sin(angle/2)
	if target==1:row=math.atan2(2*(s1*x1+y1*z1),1-2*(x1*x1+y1*y1));pitch=math.asin(2*(s1*y1-z1*x1));yaw=math.atan2(2*(s1*z1+x1*y1),1-2*(y1*y1+z1*z1));print('body z-y-x');print('yaw=',round(math.degrees(yaw),3));print('pitch=',round(math.degrees(pitch),3));print('roll=',round(math.degrees(row),3))
	else:print('q=',round(s1,3),round(x1,3),round(y1,3),round(z1,3))
elif target==2:c=math.cos(angle);s=math.sin(angle);t=1-c;r11=t*x*x+c;r12=t*x*y-s*z;r13=t*x*z+s*y;r21=t*x*y+s*z;r22=t*y*y+c;r23=t*y*z-s*x;r31=t*x*z-s*y;r32=t*y*z+s*x;r33=t*z*z+c;print('rotation matrix:');print('row1=',round(r11,3),round(r12,3),round(r13,3));print('row2=',round(r21,3),round(r22,3),round(r23,3));print('row3=',round(r31,3),round(r32,3),round(r33,3))
else:print('invalid target')