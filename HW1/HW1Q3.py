t = input('Введите шестизначный номер билета: ')
print('yas' if int(t[0])+int(t[1])+int(t[2]) == int(t[3])+int(t[4])+int(t[5]) else 'no')