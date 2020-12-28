myPets = ['rocky', 'chummy', 'Fatboy']
print('Enter a pet name: ')
name= input()
if name not in myPets:
    print("I don;t have name with :"+name)
else:
    print(name+' is my pet name')
