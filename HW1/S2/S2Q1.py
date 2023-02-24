# num = int(input('Введите число: '))
# result = 1
# while num > 1:
#     result *= num
#     num -= 1


def fact(num):
    if num == 0:
        return 1
    return num * fact(num-1)

print(fact(1))
