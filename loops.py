l1 = [1,2,3,4]
a = range(len(l1))
b = list(a)
print(b)

for i in  range(len(l1)-1,-1,-1):
    print(l1[i])

c = [*a]
print(c)
d = [x for x in a]
print(d)
