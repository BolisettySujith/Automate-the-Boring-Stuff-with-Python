catNames=[]
while True:
    print("enter the name of cat"+ str(len(catNames)+1) +"(or enter nothing to stop):",end=' ')
    name = input()
    if name == '':
        break
    catNames = catNames+[name]
print('The cat names are: ')
for name in catNames:
    print(''+name)


