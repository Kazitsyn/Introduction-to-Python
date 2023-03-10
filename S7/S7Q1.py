def find_farthest_orbit(list_of_orbits):
    tmplst = [0, 0]
    s = 0
    for i in list_of_orbits:
        a, b = i
        if a != b:
            tmp = a * b
            if tmp > s:
                s = tmp
                tmplst[0], tmplst[1] = a, b
    return tmplst


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

# return max(list_of_orbits, key = lambda i: (i[0] != i[1]) * i[0] * i[1])