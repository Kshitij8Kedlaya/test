tuplea = ("apple","orange","lemon")
print(tuple)
x = 10
str(x)

lista =  list(tuplea)
lista.append("Mango")
tuplea = tuple(lista)

print(type(lista))
for i in tuplea:
    print(i)

if "lemon" in tuplea:
    print("Lemon is there")
else:
    print("No Lemons :( ")

print(len(tuplea))

tupleb = ("Orange")
tuplec = ("Orange",)
print(type(tupleb))
print(type(tuplec))

tupled = tuplea + tuplec
print(tupled)