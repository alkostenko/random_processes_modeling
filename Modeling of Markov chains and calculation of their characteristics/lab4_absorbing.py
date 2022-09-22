import numpy as np
from matplotlib import pyplot as plt
from colorsys import hls_to_rgb

p0=[0.0,0.3,0.1,0.6]
p=np.array([1,0,0,0,0.18,0.23,0.5,0.09,0.12,0.12,0.29,0.47,0.22,0.62,0.15,0.01]).reshape((4,4))
state=[]
time=[]
currentRow=p[0]

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


state_sum=0
for i in range(100):
    state_sum+=len(state[i])
print(state_sum)


matrix=[1,0,0,0]
count=[]
moves=[]

for i in range(3):
    moves.append(0)
    count.append([])
    for j in range(4):
        count[i].append(0)
for k in range(2,5):
    for i in range(100):
        for j in range(len(state[i])):
            if state[i][j]==k:
                if state[i][j+1]==1:
                    count[k-2][0]+=1
                elif state[i][j+1]==2:
                    count[k-2][1]+=1
                elif state[i][j+1]==3:
                    count[k-2][2]+=1
                else:
                    count[k-2][3]+=1
                moves[k-2]+=1

for i in range(3):
    for j in range(4):
        matrix.append(count[i][j]/moves[i])

matrix=np.array(matrix).reshape((4,4))
print(count)
print(matrix)

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

av_time=state_sum/100
print(av_time)


sum1=0
sum2=0
sum3=0
c1=0
c2=0
c3=0

for i in range(100):
    if state[i][0]==2:
        sum1+=len(state[i])
        c1+=1
    elif state[i][0]==3:
        sum2+=len(state[i])
        c2+=1
    else:
        sum3+=len(state[i])
        c3+=1

av_time_list=[]
av_time_list.append(sum1/c1)
av_time_list.append(sum2/c2)
av_time_list.append(sum3/c3)

av_time_list=np.array(av_time_list).reshape(3,1)
print(av_time_list)

n=int(input("Введіть:"))
j=int(input("Введіть:"))

steps_j=0
steps_c=0
for i in range(100):
    if state[i][0]==n:
        steps_j+=state[i].count(j)
        steps_c+=1

if steps_c!=0:
    av_steps_j=steps_j/steps_c
else:
    av_steps_j=0

print(av_steps_j)

B=np.matmul(fundmatrix,R)
print("Ймовірність поглинання:")
print(B)