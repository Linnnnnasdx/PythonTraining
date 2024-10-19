my_list = [["a",33],["b",11],["c",55]]

# 排序，基於帶名函數
def choose_sort_key(element):
    # 依照下標1的數值進行排序
    return element[1]

my_list.sort(key=choose_sort_key,reverse=True)      # reverse 代表正序or倒序
print(my_list)

# 使用lambda匿名函數(一次性)
my_list.sort(key=lambda element: element[1],reverse=True)
print(my_list)