# 設計鬧鐘類
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

# 創建對象
clock1 = Clock()
clock1.id = "0033032"
clock1.price = 19.99
print(f"鬧鐘ID: {clock1.id},價格: {clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "006719"
clock2.price = 29.99
print(f"鬧鐘ID: {clock2.id},價格: {clock2.price}")
clock2.ring()