# 猜隨機數字，限制三次。

import random
num = random.randint(1,10)
guess_num = None
guess_count = 0
guess_limit = 3
in_the_limit = True
while guess_num != num and (in_the_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess_num = int(input("輸入你要猜的數字: "))
        if guess_num < num:
            print("你猜的數字小了")
        elif guess_num > num:
            print("你猜的數字大了")
    else:
        in_the_limit = False
if in_the_limit == True and guess_count == 1:
    print("恭喜一次答對")
elif in_the_limit == True and guess_count == 2:
    print("恭喜二次答對")
elif in_the_limit == True and guess_count == 3:
    print("恭喜三次答對")
else:
    print("你輸了，答案是 " + str(num))




# if guess_num == num:
#     print("恭喜第一次就猜對")
# else:
#     if guess_num > num:
#         print("你猜的數字大了")
#     else:
#         print("你猜的數字小了")

#     guess_num = int(input("再次輸入你要猜的數字: "))

#     if guess_num == num:
#         print("恭喜第二次就猜對")
#     else:
#         if guess_num > num:
#             print("你猜的數字大了")
#         else:
#             print("你猜的數字小了")

#         guess_num = int(input("第三次輸入你要猜的數字: "))

#         if guess_num == num:
#             print("恭喜第三次就猜對")
#         else:
#             print("你輸了，答案是 " + str(num))
        
