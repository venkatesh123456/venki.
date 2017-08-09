a=int(input(" "))
b=int(input(" "))
c=int(input(" "))
d=int(input(" "))
e=int(input(" "))
if(a>b and a>c and a>d and a>e ):
    print ('the largest num is :',a)
elif (b>a and b>c and b>d and b>c):
    print ('the largest num is :',b)
elif (c>a and c>b and c>d and c>e):
    print ('the largest num is :',c)
elif (d>a and d>b and d>c and d>e):
    print ('the largest num is :',d)
else:
    print ('the largest num is :',e)
