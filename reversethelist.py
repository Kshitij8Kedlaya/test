lista = [100,200,300,400,500]
listb = []
l = len(lista)
for i in range(l-1,-1,-1):
   x = lista[i]
   listb.append(x)

print(listb)