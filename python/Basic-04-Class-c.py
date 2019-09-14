#インスタンスメソッド（引数）
#
class MenuItem:
    def info(self):
        return self.name + ': ¥' + str(self.price)

    # get_total_priceメソッドを定義してください
    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())

# get_total_priceメソッドを呼び出してください
result = menu_item1.get_total_price(4)

# 「合計は〇〇円です」となるように出力してください
print('合計は' +  str(result) + '円です')

#=====================================================================
# __init__ メソッド
# インスタンスが生成されたときに、自動で呼び出される
class MenuItem:
    # __init__メソッドを定義してください
    def __init__(self):
        print ('MenuItemクラスのインスタンスが生成されました！')

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')

#=====================================================================
# __init__ メソッド (2)
#
class MenuItem:
    def __init__(self):
        # self.nameに「サンドイッチ」を代入してください
        self.name = 'サンドイッチ'

        # self.priceに「500」を代入してください
        self.price = 500

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
# 以下の2行は削除してください
#menu_item1.name = 'サンドイッチ'
#menu_item1.price = 500

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')

#=====================================================================
#__init__ メソッド (3): 引数を受け取る
#
class MenuItem:
    # 引数「name」と「price」を受け取るようにしてください
    def __init__(self, name, price):
        # 「サンドイッチ」の代わりに引数nameの値を代入してください
        self.name = name

        # 「500」の代わりに引数priceの値を代入してください
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


# 引数を「サンドイッチ」と「500」としてください
menu_item1 = MenuItem('サンドイッチ', 500)

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')
