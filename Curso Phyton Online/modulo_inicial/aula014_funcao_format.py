a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

formato1 = "A = {}, B = {}, C = {}".format(a, b, c) # Por ordem
print(formato1)

formato2 = "A = {2}, B = {0}, C = {1}".format(b, c, a) # Por índices
print(formato2)

formato3 = "A = {fa}, B = {fb}, C = {fc}".format(fa = a, fb= b, fc = c) # Por nomeclatura
print(formato3)
