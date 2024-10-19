#   字符串和元組一樣，不可修改

#   index
my_str = "itheima and itcast"

value = my_str.index("and")
print(value)

#   replace     不能修改，只能替換成新字符串
new_my_str = my_str.replace("it","程序")
print(f"將字符串 {my_str} 替換成 {new_my_str}")

#   split 分割
my_str = "hello python itheima itcast" 
my_str_list = my_str.split(" ")     # 用空白建作為分割
print(f"將字符串 {my_str} 進行分割後得到: {my_str_list}, 類型是: {type(my_str_list)}")