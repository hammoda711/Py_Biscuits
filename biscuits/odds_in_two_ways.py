'''
list tcomperhension
s=[9,8,5]
odds = [x for x in s if x % 2 != 0 ]
print(odds)
'''
odds=[]
s=[9,8,5]
for x in s:
    if x % 2 != 0:
        odds.append(x)
        print(odds)