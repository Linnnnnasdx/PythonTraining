"""和文件相關的類別定義"""

from data_define import Record
import json

# 先定義一個抽象類做頂層數據，確定有哪些功能需要實現

class FileReader:

    def read_data(self) -> list[Record]:
        """讀取文件的數據，讀到的每一條數據都轉換為Record對象，將它們都封裝到list內返回即可"""
        pass

# 定義兩個子類做實際操作，一個讀csv，一個讀json
class TextFileReader(FileReader):

    def __init__(self,path):
        self.path = path        # 定義成員變量，用來紀錄文件路徑

    # 覆寫(實現抽象方法)父類的方法
    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list:list[Record] = []

        for line in f.readlines():
            line = line.strip()         # 移除首尾空格及換行符號，或特定字符串
            data_list = line.split(",")         # 用 ',' 進行分割成list
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)
        
        f.close()
        return record_list


class JsonFileReader(FileReader):
    def __init__(self,path):
        self.path = path


    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="UTF-8")
        record_list:list[Record] = []

        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"], data_dict["order_id"], int(data_dict["money"]), data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list


if __name__ == '__main__':
    text_file_reader = TextFileReader("C:/Users/LEGION/Desktop/python學習教材/资料/第13章/2011年1月销售数据.txt")
    json_file_reader = JsonFileReader("C:/Users/LEGION/Desktop/python學習教材/资料/第13章/2011年2月销售数据JSON.txt")
    list1 = text_file_reader.read_data()
    list2 = json_file_reader.read_data()


    for l in list1:
        print(l)

    for l in list2:
        print(l)