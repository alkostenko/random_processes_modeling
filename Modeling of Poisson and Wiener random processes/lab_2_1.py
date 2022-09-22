#Task 1: Poisson process
from matplotlib import pyplot as plt
import math
import random
import statistics
import numpy as np
from colorsys import hls_to_rgb

def factorial(n):
    if n==0:
        return 1
    else:
        fact=1
        for i in range(1,n+2):
            fact=fact*i
        return(fact)


n=5
m=100
l=3
s=[]
t=[]
x_values=[]
y_values=[]
for i in range(n):
    s.append([])
    x_values.append([])
    y_values.append([])

for i in range(n):
    s[i].append(0)
    for j in range(1,m):
        s[i].append(-(1/l)*np.log(1-random.random()))


fig, ax=plt.subplots(figsize=(8,6))
hue=0/360
luminosity= 0.5
saturation=1
leg=[]
for i in range(n):
    x_prev=0
    for j in range(m-1):
        x=x_prev+s[i][j+1]
        x_values[i].extend([x_prev,x])
        y_values[i].extend([j,j])
        x_values[i].extend([x,x])
        y_values[i].extend([j,j+1])
        x_prev+=s[i][j+1]

for i in range(n):
    hue+=70/360
    color=hls_to_rgb(hue, luminosity, saturation)
    ax.plot(x_values[i],y_values[i], color=color, label=str(i+1)+"-та подія")
    ax.legend()
plt.xlabel("Час")
plt.title("Реацізації Поуссонівського поцесу")
plt.show()


#_____1_____
#???????????????????????
k=2
p=[]

ktime=[]
for i in range(m):
    ksum=0
    lower_lim=(i-1)*k
    upper_lim=lower_lim+k
    for j in range(lower_lim, upper_lim):
        ksum+=math.exp(-l*s[k][i])*l*s[k][i]
    ktime.append(ksum)

plt.hist(ktime, color="purple", edgecolor="black")
plt.show()
#_____2_____
s1=[]
for i in range (n):
    s1.extend(s[i])

plt.hist(s1, color="lightblue", edgecolor="black")
plt.xlabel("Інтервал")
plt.ylabel("Часота")
plt.title("Розподіл інтервалу між подіями")
plt.show()


#_____3_____
mid=n/l
time=[]
for j in range(m):
    current=0
    for i in range(n):
        current+=s[i][j]
    time.append(current)

plt.xlabel("Час")
plt.ylabel("Часота")
plt.title("Розподіл появи n подій")    
plt.hist(time, color="red", edgecolor="black")
plt.show()


