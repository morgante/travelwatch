import random
import numpy as np

dat=[]
lindist=[]
for i in range(10):
    for j in range(i):
        lindist.append(i+1)

for i in range(100):
    temp=[]
    temp.append(i)

    j = random.randint(1,10)
    
    for i in range(10):
        temp.append(j)

    temp.append(j)

    # su=float(np.sum(temp[1:]))

    # for n in range(1,len(temp)):
        # temp[n]=temp[n]/su
    
    # if np.sum(temp[1:5])>=0.4:
    #     temp.append(random.choice(lindist))
    # else:
    #     temp.append(11-random.choice(lindist))
    
    dat.append(temp)
    

np.savetxt("train.csv",np.array(dat), delimiter=',')