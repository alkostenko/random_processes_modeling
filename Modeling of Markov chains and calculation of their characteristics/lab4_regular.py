import numpy as np
from matplotlib import pyplot as plt
from colorsys import hls_to_rgb


p=np.array([0.4,0.33,0.27,0.79,0.13,0.08,0.27,0.41,0.32]).reshape((3,3))
p0=[0.04,0.42,0.54]


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


step_sum=100*10


matrix=[]
count=[]
moves=[]

for i in range(3):
    moves.append(0)
    count.append([])
    for j in range(3):
        count[i].append(0)
for k in range(1,4):
    for i in range(100):
        for j in range(9):
            if state[i][j]==k:
                if state[i][j+1]==1:
                    count[k-1][0]+=1
                elif state[i][j+1]==2:
                    count[k-1][1]+=1
                elif state[i][j+1]==3:
                    count[k-1][2]+=1
                else:
                    count[k-1][3]+=1
                moves[k-1]+=1

for i in range(3):
    for j in range(3):
        matrix.append(count[i][j]/moves[i])

matrix=np.array(matrix).reshape((3,3))

print(matrix)


#Матриця фінальних імовірностей
wcurrent=np.around(np.matmul(p0, np.linalg.matrix_power(matrix,1)),7)

for i in range(2,15):

        wnext=np.around(np.matmul(p0, np.linalg.matrix_power(matrix,i)), 7)
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


#Фундаментальна матриця
I=np.array([1,0,0,0,1,0,0,0,1]).reshape((3,3))
Z=np.linalg.matrix_power(np.subtract(I,np.subtract(p,W)),-1)
print("Фундаментальна матриця:")
print(Z)

#Середній час перебування в заданому стані за n=4 кроків
state_n4=[]
for i in range(3):
    state_n4.append(0)

for i in range(100):
    for j in range(4):
        if state[i][j]==1:
            state_n4[0]+=1
        elif state[i][j]==2:
            state_n4[1]+=1
        else:
            state_n4[2]+=1

for i in range(3):
    state_n4[i]/=100

state_n4=np.array(state_n4).reshape(3,1)
print(state_n4)

#Середній час виходу ланцюга в заданий стан (в стан j , коли процеспочався зі стану n)
n=int(input("Введіть:"))
j=int(input("Введіть:"))
jsum=0
jcount=0

for i in range(100):
    if state[i][0]==n:
        if j in state[i]:
            jsum+=state[i].index(j)
            jcount+=1
        else:
            pass
    
print(jsum/jcount)


#Середній час виходу ланцюга в заданий стан (коли початковий стан не заданий)

jsum=0
jcount=0

for i in range(100):
    if j in state[i]:
        jsum+=state[i].index(j)
        jcount+=1
    else:
        pass

print(jsum/jcount)

