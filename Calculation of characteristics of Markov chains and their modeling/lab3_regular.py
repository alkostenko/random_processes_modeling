import numpy as np
import networkx as nx
import pandas as pd
import random 
from matplotlib import pyplot as plt
from colorsys import hls_to_rgb

#__Task2_______
#1
p=np.array([0.4,0.33,0.27,0.79,0.13,0.08,0.27,0.41,0.32]).reshape((3,3))
p0=[0.04,0.42,0.54]

print("Матриця переходів:")
print(p)

#2
wcurrent=np.around(np.matmul(p0, np.linalg.matrix_power(p,1)),7)

for i in range(2,15):

        wnext=np.around(np.matmul(p0, np.linalg.matrix_power(p,i)), 7)
        isequal=(wcurrent==wnext).all()
        if isequal==True:
            wline=wnext
            k=i-1
            break

        wcurrent=wnext  

W=[]
for i in range(3):      
    W.append(wline)

W=np.array(W).reshape((3,3))
print("Матриця фінальних ймовірностей:")
print(W)

#3
I=np.array([1,0,0,0,1,0,0,0,1]).reshape((3,3))
Z=np.linalg.matrix_power(np.subtract(I,np.subtract(p,W)),-1)
print("Фундаментальна матриця:")
print(Z)

#5
E=np.array([1,1,1,1,1,1,1,1,1]).reshape((3,3))
D=[]
Zdg=[]
for i in range(9):
    D.append(0.0)
    Zdg.append(0.0)
D=np.array(D).reshape((3,3))
Zdg=np.array(Zdg).reshape((3,3))

for i in range(3):
    D[i][i]=1/wline[i]
    Zdg[i][i]=Z[i][i]


M=np.matmul(np.add(np.subtract(I,Z),np.matmul(E,Zdg)),D)
print("Матриця середньої кількості кроків:")
print(M)

j=int(input("Введіть стан, у який здіснюється перехід (нумерація починається з 1): "))
n=int(input("Введіть стан, з який здіснюється перехід (нумерація починається з 1): "))
m=M[n-1][j-1]
print("Середній час виходу ланцюга в заданий стан:")
print(m)

#6
m1=[] 
for i in range(3):
    m1.append(M[i][j-1])
print("Середній час виходу ланцюга в заданий стан (коли початковий стан не задано):")
print(m1)

#7
Wdg=[]
for i in range(9):
    Wdg.append(0.0)

Wdg=np.array(Wdg).reshape((3,3))

for i in range(3):
    Wdg[i][i]=W[i][i]

Mw=np.matmul(np.add(np.subtract(I,W),np.matmul(E,Wdg)),D)
mw=[]
for i in range(3):
    mw.append(Mw[i][j-1])
print("Середній час виходу ланцюга в заданий стан в стаціонарному режимі:")
print(mw)


#___Task4___
state=[]
fig, ax=plt.subplots(figsize=(10,6))
hue=0
luminosity= 0.5
saturation=1
time=[]
for i in range(10):
    time.append(i)


for i in range(100):
    hue+=1/10
    color=hls_to_rgb(hue, luminosity, saturation)
    state.append([])
    currentRow=p0
    for j in range(10):
        x=np.random.uniform(0.0,1.0)
        if x>=0 and x<currentRow[0]:
            k=1
            currentRow=p[0]
        elif x>=currentRow[0] and x<(currentRow[1]+currentRow[0]):
            k=2
            currentRow=p[1]
        else:
            k=3
            currentRow=p[2]
        state[i].append(k)
    ax.plot(list(time),list(state[i]), color=color, label=str(i+1)+"-ий ряд")

plt.grid()
plt.show()