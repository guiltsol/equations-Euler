#Программа которая находит максимальную сумму делителей максимального числа из отрезка 
n1=int(input())
n2=int(input())
arr1=[x for x in range(n2,n1-1,-1)]
print(arr1)
arr=[]
su=0
for i in range(n2,n1-1,-1):
    for j in range(i,0,-1):
        if i%j==0:
            su+=j
    print('symm',su)
    arr.append(su)
    su=0
mx=max(arr)
ind=arr.index(mx)
print(arr1[ind],mx)