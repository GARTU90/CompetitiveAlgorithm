a,b=map(int,input().split())
c=list(map(int,input().split()))
c.sort()
#busquedaBinaria
d=0
e=a-1
g=0
while e>=d:
 # print("e",e,"f",f)
  f=(e+d)//2
  if c[f]==b:
    print(b)
    break
  if c[f]<b:
    d=f +1

    g=c[f]
  if c[f]>b:
    e=f-1
if c[f]!=b:
  print(g)
