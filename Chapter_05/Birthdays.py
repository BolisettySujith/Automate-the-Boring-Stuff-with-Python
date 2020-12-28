birthdays ={'sujith':'15oct','Banti':'16Dec','lucky':'9nov'}

while True:
    print('Enter a name :')
    name = input()
    if name =='':
        break

    if name in birthdays:
        print(birthdays[name] +' is the birthday of'+ name)
    else:
        print('i do not have birthday info for name '+ name)
        print('Whaty is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday updated')

