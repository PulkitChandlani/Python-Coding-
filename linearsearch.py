def ls(lst,n,x):
    for i in range(0,n):
        if(lst[i]==x):
            return i
    return -1

lst=[1,2,3,4,5,6,7,8]
x=7
n=len(lst)
result=ls(lst,n,x)
if(result==-1):
    print("Element not found")
else:
    print("Element found at index: ",result)
