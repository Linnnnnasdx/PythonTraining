# for y in range(1,10):
#     for x in range (1,10):
#         if y >= x:
#             print(f"{x}*{y}={x*y}\t",end='')
#     print()

for y in range(1,10):
    for x in range(1,y+1):
        print(f"{x}*{y}={x*y}\t",end='')
    print()