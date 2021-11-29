names = []
for x in range (10):
    acceptedName = input(str("Names:"))
    names.append(acceptedName)
for x in range(len(names)):
    print(names.pop(0))
