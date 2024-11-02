def find_most_frequent(nums):
    most_frequent = max(nums, key=nums.count)      # key代表要比較的值，這邊指的是此元素在列表中的數量
    count = nums.count(most_frequent)
    print("重複最多的數字:", most_frequent)
    print("出現次數:", count)

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
find_most_frequent(nums)