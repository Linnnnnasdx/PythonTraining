import json
# json.dumps(data)    將 python 數據轉成 json
# json.loads(data)    將 json 轉成 python 數據
# ensure_ascii=False    確保中文正常轉換 

# 準備列表，列表內每個元素都是字典，將其轉換為json
data = [{"name":"林","age":21},{"name":"Jay","age":11},{"name":"kuan","age":30}]
json_str = json.dumps(data,ensure_ascii=False)
print(type(json_str))
print(json_str)

d = {"name":"周杰倫","addr":"台北"}
json_str = json.dumps(d,ensure_ascii=False)
print(json_str)

# 將 json 字串轉為 python 數據類型
s = '[{"name":"林","age":21},{"name":"Jay","age":11},{"name":"kuan","age":30}]'
l = json.loads(s)
print(type(l))
print(l)

s = '{"name":"周杰倫","addr":"台北"}'
d = json.loads(s)
print(type(d))
print(d)