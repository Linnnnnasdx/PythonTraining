t1 = (1,"hello",True)       #Tuple用小括號
t2 = ("hello", )        #Tuple若只有一個數據，一定要加一個'逗號'\

tuple = ('周杰倫',11,['football','music'])

print(tuple.index(11))

print(tuple[0])

del tuple[2][0]
print(tuple)

tuple[2].append('coding')
print(tuple)