def l(a,t):
  for i in range(len(a)):
    if a[i] == t:
      return i
  return -1
d=[7,2,9,4,1,5]
t=4
r=l(d,t)
print("Found at index:",r if r!=-1 else "not found")
