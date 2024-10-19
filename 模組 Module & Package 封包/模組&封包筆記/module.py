# 模組就是一個python文件，裡面有類、函數、變量等，可以拿過來用(導入)，像是一個工具箱

# 使用 import 導入 time 模塊
import time     # python內建time.py模組
print("你好")
time.sleep(5)
print("我好")

# 使用 from 導入 time 裡面的 sleep 功能(函數)
from time import sleep
print("你好")
sleep(5)        # 可以直接輸入函數名
print("我好")

# 使用 * 導入 time 模塊的全部功能
from time import *
print("你好")
sleep(5)        # 可以直接輸入函數名
print("我好")

# 使用 as 給特定功能加上別名
import time as t
print("你好")
sleep(5)
print("我好")

from time import sleep as sl
print("你好")
sl(5)
print("我好")