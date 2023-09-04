a = input("Enter Something: ")
b = {}
a = a.lower()


for i in a:
    if i != " ":
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
print(b)