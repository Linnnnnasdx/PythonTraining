class phone:
    __is_5g_enable = True

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5G開啟")
        else:
            print("5G關閉，使用4G網路")

    def call_by_5g(self):
        self.__check_5g()
        print(self.__is_5g_enable)
        print("正在通話中") 

p = phone()
p.call_by_5g()