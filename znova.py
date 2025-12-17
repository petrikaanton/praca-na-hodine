import random

def generuj(n:int) -> list:
    zoz=[]
    for i in range(n):
        zoz.append(random.randint(1,100))
    return zoz
moj_zoznam=generuj(10)
print(moj_zoznam)

for i in range(len(moj_zoznam)-1,0,-1):
    moj_max=moj_zoznam[0]
    moj_index=0
    for j in range(1,i+1):
        if moj_zoznam[j]>moj_max:
            moj_max=moj_zoznam[j]
            moj_index=j
    moj_zoznam[moj_index], moj_zoznam[i] = moj_zoznam[i], moj_zoznam[moj_index]

print(moj_zoznam)
