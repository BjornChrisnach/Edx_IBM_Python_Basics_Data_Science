import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

a_np_list = np.array([0,1,2,3,4])

a_np_list.size:5
a_np_list.ndim:1
a_np_list.shape: (5,)

b = np.array([3.1,11.02,6.2,213.2,5.2])
print(type(b)) # :numpy.ndarray
b.dtype:np.dtype("float64")

c = np.array([20,1,2,3,4])
c:np.array([20,1,2,3,4])
c[0]=100
c:np.array([100,1,2,3,4])
c[4]=0
c:np.array([100,1,2,3,4])
d=c[1:4]
d:np.array([1,2,3])
c[3:5]=300,400
c:np.array([0,1,2,300,400])

u=[1,0]
v=[0,1]
z=[]
for n, m in zip(u,v):
    z.append(n+m)

u=np.array([1,0])
v=np.array([0,1])
z=u+v
z:np.array([1,1])

u=[1,0]
v=[0,1]
z=[]
for n, m in zip(u,v):
    z.append(n-m)

u=np.array([1,0])
v=np.array([0,1])
z=u-v
z:np.array([1,1])

y=np.array([1,2])
z=2*y
z:np.array([2,4])

y=[1,2]
z=2*y
for n in y:
    z.append(2*n)

u=np.array([1,2])
v=np.array([3,2])
z=u*v
z:np.array([3,4])

u=[1,2]
v=[3,2]
z=[]
for n, m in zip(u,v):
    z.append(n*m)

u=np.array([1,2])
v=np.array([3,1])
result=np.dot(u,v)
result:5

u=np.array([1,2,3,-1])
z=u+1
z:np.array([2,3,4,0])

a=np.array([1,-1,1,-1])
mean_a=a.mean
mean_a=0.0

a=np.array([1,4])
z=a*(1-1+1-1)
z=0

b=np.array([1,-2,3,4,5])
max_b=b.max()
max_b:5

np.pi
x=np.array([0,np.pi/2,np.pi])
y=np.sin(x)
y:np.array([0,1,1.2e-16])

np.linspace(-2,2,num=5)
np.linspace(-2,2,num=9)

x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
plt.plot(x,y)
plt.show()