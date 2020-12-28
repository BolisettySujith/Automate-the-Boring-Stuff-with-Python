def isPhoneNumber(text):
    if len(text) !=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] !='-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-' :
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

print('Is 415-555-4242 a phone number')
print(isPhoneNumber(num))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

message = 'call me at 132-546-1459 tommorow. 458-658-7526 is my ooffice .'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: '+ chunk)
    print('Done')