import time
def calProd():
    product = 1
    for i in range(1,1000):
        product = product * i
        return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('This result is %s digit long .'%(len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))