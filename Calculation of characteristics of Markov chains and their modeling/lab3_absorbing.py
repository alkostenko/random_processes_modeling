#______Task1______

#1
import numpy as np
from matplotlib import pyplot as plt
from colorsys import hls_to_rgb



p0=[0.0,0.3,0.1,0.6]
p=[1,0,0,0,0.18,0.23,0.5,0.09,0.12,0.12,0.29,0.47,0.22,0.62,0.15,0.01]
shape=(4,4)
matrix=np.array(p).reshape(shape)
print(matrix)

#2
I=[]
O=[]
R=[]
Q=[]
I=matrix[0][0]
O=matrix[0][1:4]
for i in range(1,4):
    R.append(matrix[i][0])
    Q.append(matrix[i][1])
    Q.append(matrix[i][2])
    Q.append(matrix[i][3])
R=np.array(R).reshape((3,1))
Q=np.array(Q).reshape((3,3))
E=np.array([1,0,0,0,1,0,0,0,1]).reshape((3,3))
IminusQ=np.subtract(E,Q)
print(IminusQ)
fundmatrix=np.linalg.matrix_power(IminusQ,-1)
fundmatrix=np.matrix.round(fundmatrix, 3)
print("Фундаментальна матриця:")
print(fundmatrix)

#3

#4

#5
m1=[[1],[1],[1]]
time=np.matmul(fundmatrix,m1)
print("Середній час поглинання:")
print(time)

#6
B=np.matmul(fundmatrix,R)
print("Ймовірність поглинання:")
print(B)



#______Task3_________


p=np.array([1,0,0,0,0.18,0.23,0.5,0.09,0.12,0.12,0.29,0.47,0.22,0.62,0.15,0.01]).reshape((4,4))
state=[]
time=[]
currentRow=p[0]


for i in range(100):
    state.append([])

def first(state,i):
    x=np.random.uniform(0.0,1.0)
    if x<p0[1]:
        k=2
        currentRow=p[1]
    elif x>=p0[1] and x<p0[2]+p0[1]:
        k=3
        currentRow=p[2]
    else:
        k=4
        currentRow=p[3]

    state[i].append(k)
    result=[]
    result.append(k)
    result.append(currentRow)
    return result

for i in range(100):
    k=first(state,i)[0]
    currentRow=first(state,i)[1]
    while k!=1:
        x=np.random.uniform(0.0,1.0)
        if x<currentRow[0]:
            k=1
            state[i].append(k)
            break
        elif x>=currentRow[0] and x<currentRow[1]+currentRow[0]:
            k=2
            currentRow=p[1]
        elif x>=currentRow[1] and x< currentRow[2]+currentRow[1]:
            k=3
            currentRow=p[2]
        else:
            k=4
            currentRow=p[3]
        state[i].append(k)



hue=0
fig=plt.subplots(figsize=(10,6))
plt.grid()

for i in range(len(state)):
    time=[]
    for j in range(len(state[i])):
        time.append(j)
    hue+=0.05
    color=hls_to_rgb(hue, 0.5, 1)
    plt.plot(time, state[i], color=color)


plt.show()