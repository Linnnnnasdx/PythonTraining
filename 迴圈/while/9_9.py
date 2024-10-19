i = 1

while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t", end='')   #\t能夠對齊、end=''代表不要換行
        j += 1
    i += 1
    print() #代表換行