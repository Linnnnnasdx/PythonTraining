# name = "itheima is a vrand of itcast"
# sum = 0
# for x in name:
#     if x == "a":
#         sum += 1
# print(f"總共有{sum}個a")

# def check (x):
#     if x <= 37.5:
#         print(f"你的體溫是{x}，正常請進")
#     else:
#         print(f"你的體溫是{x}，需要隔離")

# check(37.6)

def check_age(age):
    if age > 18:
        return "SUCCESS"
    else:
        return None

result = check_age(19)
if not result:      #如果 result 為 False(None)
    print("未成年")