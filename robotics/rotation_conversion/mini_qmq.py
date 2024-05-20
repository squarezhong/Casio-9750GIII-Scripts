s1,x1,y1,z1=map(float,input('s1 x1 y1 z1=').split())
s2,x2,y2,z2=map(float,input('s2 x2 y2 z2=').split())
s=s1*s2-x1*x2-y1*y2-z1*z2
x=s1*x2+x1*s2+y1*z2-z1*y2
y=s1*y2+y1*s2+z1*x2-x1*z2
z=s1*z2+z1*s2+x1*y2-y1*x2
print('q=',round(s,3),round(x,3),round(y,3),round(z,3))