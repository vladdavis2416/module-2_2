first= input("Введите первое число:")
second= input("Введите второе число:")
third= input("Введите третье число:")

if first==second==third:    print(3)
if first==second or second==third or first==third:   print(2)
else: print(0)
