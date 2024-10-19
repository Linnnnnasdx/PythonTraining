def print_file_info(file_name):
    f = None
    try:
        f = open(file_name,"r",encoding="UTF-8")
        content = f.read()
        print("全部內容如下:")
        print(content)
    except Exception as e:       # 捕獲全部異常
        print(f"找不到文件!原因是{e}")
    finally:
        if f :       # 如果變量是None,表示 Fales；如果有任何內容,就是 True
            f.close()

def append_to_file(file_name,data):
    f = open(file_name,"a",encoding="UTF-8")
    f.write(data)
    f.close()

if __name__ == '__main__':
    append_to_file("D:/python training/模組 Module & Package 封包/my_utils/test.txt","\n水水水")