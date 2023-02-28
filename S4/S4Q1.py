st  =  'a a a b c a a d c d d'
lt = st.split()
print(lt)
dct = {}
output = ''
for i in lt:
    if i in dct:
        dct[i] += 1
        output += f'{i}_{dct[i]} '
    else:
        dct[i] = 0
        output += f'{i} '
print(dct)
print(output)