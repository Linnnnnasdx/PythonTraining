from typing import Union

my_list:list[Union[int,str]] = [1,2,"LIN","YYY"]        # 會傳入int 或是 str

def func(data: Union[int,str]) -> Union[int,str]:
    pass

func()