# 自定義模組

__all__ = ["test_A"]        # __all__變量可以影響使用import * 可導入的函數

def test_A(a,b):
    print(a+b)

def test_B(a,b):
    print(a-b)

if __name__ == '__main__':      #__main__ 變量可以測試模塊
    test_A(1,2)
