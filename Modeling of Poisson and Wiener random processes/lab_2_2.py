#Task 2:Wiener process
#___1___
import math
import numpy as np 
from matplotlib import pyplot as plt
from numpy.lib.function_base import average
m=1000
mu0=np.random.normal(0,1)
mu1=list(np.random.normal(0,1,m))
mu2=[]
mu2.append(mu1[0])
mu2.append(list(np.random.normal(0,1,m)))
mu2.append(list(np.random.normal(0,1,m)))



x=[]
w1=[]
w2=[]
for i in range(m):
        x.append(i/m)

for i in range(m):
    sum1=0
    sum2=0
    for j in range (1,m):
        sum1+=math.sin(j*math.pi*x[i])*mu1[j]/(j*math.pi)
        sum2+=math.sin(2*j*math.pi*x[i])*mu2[1][j]/(2*j*math.pi)+(1-math.cos(2*j*math.pi*x[i]))*mu2[2][j]/(2*j*math.pi)  
    w1_value=x[i]*mu0+math.sqrt(2)*sum1
    w2_value=x[i]*mu0+math.sqrt(2)*sum2 
    w1.append(w1_value) 
    w2.append(w2_value)

fig, ax=plt.subplots(figsize=(8,6))
ax.plot(x, w1, color="red")
ax.plot(x, w2, "b--")
plt.show()

w1=[]
w1_list=[]
#___2___
for j in range (10):
    mu0=np.random.normal(0,1)
    mu1=list(np.random.normal(0,1,m))
    for i in range(m):
        sum1=0
        sum2=0
        for j in range (1,m):
            sum1+=math.sin(j*math.pi*x[i])*mu1[j]/(j*math.pi)
        w1_value=x[i]*mu0+math.sqrt(2)*sum1
        w1.append(w1_value) 
    w1_list.append(w1)

d=[]
disp=[]
avr=[]
for i in range (m):
    s=0
    for j in range(10):
        d.append(w1_list[j][i])
        s+=w1_list[j][i]
    avr.append(s/100)
    disp.append(np.var(d))
plt.subplot(1,2,1)
plt.plot(x, avr, color="red", label="Середнє значення")
plt.title("Графік середнього значення")
plt.subplot(1,2,2)
plt.plot(x, disp, color="blue", label="Диспесія")
plt.title("Графік дисперсії")
plt.show()


#____3____
a=float(input("Введіть бажаний рівень: "))
t=[]
for i in range(10):
    for j in range(m):
        if w1_list[i][j]>=a:
            index=j
            t.append(index/m)
            pass
plt.hist(t, color="green")
plt.show()




