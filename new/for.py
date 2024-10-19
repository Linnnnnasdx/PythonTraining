#取次方

def power(base_num,pow_num):
    result = base_num
    for index in range(pow_num-1):
        result = result*base_num
    return result

print(power(2,6))