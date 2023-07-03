line = input("Line: ")
a = line.split()
if "robot" in a:
  print("There is a small robot in the line.")
elif "ROBOT" in a:
  print("There is a big robot in the line.")
elif "robot" in line.split():
  print("There is a medium sized robot in the line.")

else:
  print("No robots here.")