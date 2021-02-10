# Atcoder Beginer's selection ABC086A

'''
s = input()
tokens = s.split
a = int(tokens[0])
b = int(tokens[1])
'''
a,b = map(int, innput().split())
if a*b%2 == 0:
    print('Even')
else:
    print('Odd')