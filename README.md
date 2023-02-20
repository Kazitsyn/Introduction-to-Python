# Introduction-to-Python
## Home Work 1
***
### Задача 2:
 *Найдите сумму цифр трехзначного числа.*

*Пример:*

123 -> 6 (1 + 2 + 3)

100 -> 1 (1 + 0 + 0) |

Решение:

```python
num = input('Введите трехзначное число: ')
print(f'{num} -> {int(num[0])+int(num[1])+int(num[2])} ({num[0]}+{num[1]}+{num[2]})')
```
Вывод консоли:
```python
Введите трехзначное число: 123
123 -> 6  (1+2+3)
```
***
### Задача 4: 
*Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?*

*Пример:*

6 -> 1  4  1

24 -> 4  16  4

60 -> 10  40  10

Решение:
```python
s = int(input('Введите количество сделанных журавликов: '))

Katya = int(s/6*4)
Petya = int(s/6)
Seryozha = int(s/6)

print(f'{s} -> {Petya} {Katya} {Seryozha}')
```
Вывод консоли:
```python
Введите количество сделанных журавликов: 24
24 -> 4 16 4
```
***
### Задача 6: 
*Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.*

*Пример:*

385916 -> yes

123456 -> no

Решение:
```python
t = input('Введите шестизначный номер билета: ')
print('yas' if int(t[0])+int(t[1])+int(t[2]) == int(t[3])+int(t[4])+int(t[5]) else 'no')
```

Вывод консоли:
```python
Введите шестизначный номер билета: 385916
yas
```
***
### Задача 8: 
*Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).*

*Пример:*

3 2 4 -> yes

3 2 1 -> no

Решение:
```python
n = int(input('n = '))
m = int(input('m = '))
k = int(input('k = '))
if k < m*n and k % m == 0 or k < m*n and k % n == 0:
    print('yas')
else:
    print('no')
```

Вывод консоли:
```python
n = 3
m = 2
k = 4
yas
```
***