#   分割字符串

mm = "itheima itcast boxuegu"

count = mm.count("it")
print(count)

new_mm = mm.replace(" ","|")
print(new_mm)

newnew_mm = new_mm.split("|")
print(newnew_mm)