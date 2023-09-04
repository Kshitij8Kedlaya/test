dances = ['ballet', 'tap', 'jazz', 'belly', 'contemporary', 'ballroom', 'salsa', 'step', 'swing', 'irish', 'modern', 'shuffle', 'floss', 'twisting', 'macarena', 'interpretive', 'wobble', 'flick', 'stomp', 'tango']

def viral_check(a):
  level = ''
  count = 0
  lista = []
  e = a.split(" ")
  run = True
  for i in e:
    b = len(i)
    if i in dances:
      level = 'nowhere, the dance already exists!'
      run = True
    elif b == 8:
      level = "not viral"
      run = True
    elif b < 4:
      level = 'slightly viral!'
      run = True
    elif "j" in i:
      level = "somewhat viral"
      run = True
    else:
      run = False
      count = count + 1
  if run == True:
     lista.extend([i,level])
  return lista , count

a = input("Enter names: ")
lista , count = viral_check(a)

d = len(lista)
for i in range(0, d, 2):
  print(f"The'{lista[i]}' will go {lista[i+1]}")
print(f"Ultra Viral names: {count}")