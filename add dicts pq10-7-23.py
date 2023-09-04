a = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
b = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}



for i,j in b.items():
    if i not in a:
        a[i] = j
    


print(a)
