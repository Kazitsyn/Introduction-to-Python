# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

import random

n = int(input('n = '))
coin = (['eagle', 'tail'])
table = []
while n > 0:
    table.append(random.choice(coin))
    n -= 1
print(table)

eagle = tail = 0
for i in table:
    if i == 'eagle':
        eagle += 1
    else:
        tail += 1
        
print(eagle if eagle <= tail else tail)
