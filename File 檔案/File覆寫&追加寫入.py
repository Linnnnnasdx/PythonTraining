f = open("D:/test.txt","w",encoding="UTF-8")
f.write("helloworld")       # 內容寫入內存中
f.flush()       # 將內存中積攢的內容，寫入到硬盤的文件中
f.close()       # 關閉將自動帶有flush()功能

f = open("D:/test.txt","a",encoding="UTF-8")

f.write("\n123")
f.close()