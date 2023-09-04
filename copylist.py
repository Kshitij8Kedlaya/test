alist = [1,3,5,7,9]
blist = alist.copy()
clist = list(blist)

print(alist)
print(blist)
print(clist)
print(list(enumerate(alist, start= 1)))