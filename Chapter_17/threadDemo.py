import threading, time
print('Stat program')

def takeaNap():
    time.sleep(5)
    print('Wake up!!!')
    print('End Program!!!')

threadObj = threading.Thread(target = takeaNap)
threadObj.start()

