import re
stu = input()
phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
kk = phoneNum.search(stu)
print('Phone number found:'+kk.group())

