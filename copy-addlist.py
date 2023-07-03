alist = [1,3,5,7,9]
blist = alist.copy()
clist = list(blist)
dlist = ["a","b","c","d","e"]
elist = clist + dlist
alist = alist + blist
for i in dlist:
    clist.append(i)
alist.extend(dlist)

print(alist)
print(blist)
print(clist)
print(elist)