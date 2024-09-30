name = set()
While True:
name = input("Give your name: ")
if name == "":
for name in names:
print(name)
break
 elif name in names:
       print ("Name exists")
       else:
       Print("New name")
       names.add(name)