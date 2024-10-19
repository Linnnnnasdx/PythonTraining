secrect_num = 87
guess_num = None
guess_count = 0
guess_limit = 3
in_the_limit = True

while secrect_num != guess_num and (in_the_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess_num = int(input("請輸入您猜測的數字: "))
        if guess_num > secrect_num and guess_num - secrect_num >= 15 :
            print("答錯~再往下!!")
        elif guess_num > secrect_num and 1 <= guess_num - secrect_num < 14 :
            print("答錯~不過答案接近了，再往下一點!")
        elif guess_num < secrect_num and guess_num - secrect_num <= -15 :
            print("答錯~再往上!!")
        elif guess_num < secrect_num and -1 >= guess_num - secrect_num > -14 :
            print("答錯~不過答案很接近了，再往上一點!")
    else:
        in_the_limit = False
if in_the_limit == True:
    print("\n !!! 恭喜答對 !!! \n")
else:
    print("\n你輸了~ \n")