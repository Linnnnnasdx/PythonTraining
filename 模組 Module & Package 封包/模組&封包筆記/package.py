# 三種方式導入封包內的函數方法

# 1.
import my_package.module1
import my_package.module2
my_package.module1.info_print1()
my_package.module2.info_print2()

# 2.
from my_package import module1
from my_package import module2
module1.info_print1
module2.info_print2

# 3.
from my_package.module1 import info_print1
from my_package.module2 import info_print2
info_print1()
info_print2()

# 從第三方安裝封包 : 到 cmd 輸入 pip install 封包名稱