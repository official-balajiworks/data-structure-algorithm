def b(a,t):
  l,h=0,len(a)-1
  while l<=h:
    m=(l+h)//2
    if a[m] == t:
      return m
    elif a[m] < t:
      l=m+1
    else:
      h=m-1
  return -1
d=[1,2,5,4,6,9,8,7]
t=4
c=sorted(d)
r=b(c,t)
print("found at index:",r if r!=-1 else "not found")
