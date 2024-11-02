def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # 找到中間索引， // 可以忽略小數點

        if arr[mid] == target:  # 找到目標值
            return mid
        elif arr[mid] < target:  # 目標值在右邊
            left = mid + 1
        else:  # 目標值在左邊
            right = mid - 1

    return -1  # 如果找不到目標值，返回 -1


arr = [1, 3, 5, 7, 9]
target = 3
result = binary_search(arr, target)

if result != -1:
    print(f"找到目標值，索引位置為: {result}")
else:
    print("目標值不存在於數列中")