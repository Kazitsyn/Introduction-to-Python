# Introduction-to-Python
Introduction to Python
*** 
## Home Work 1
### Task 2
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
