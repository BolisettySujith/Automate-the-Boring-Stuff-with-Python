def collatz(kk):
    print('Collatz the input number will run until 1')
    if kk ==1 :
        print('Collatz Completed!!!!!')
    elif kk %2 ==0:
        print(kk/2) 
        collatz(kk/2)
    else:
        print(3*kk+1)
        collatz(3*kk+1)

try :
    print (collatz(int(input('Enter a number greater than 1 :'))))
except ValueError :
    print('The number should be greater than 1 ')

    




