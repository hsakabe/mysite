# 複数のインスタンス
# menu_item1, menu_item2
class MenuItem:
    pass

menu_item1 = MenuItem()

menu_item1.name = 'サンドイッチ'
print(menu_item1.name)

menu_item1.price = 500
print(menu_item1.price)

# MenuItemクラスのインスタンスを生成してください
menu_item2 = MenuItem()

# menu_item2のnameに「チョコケーキ」を代入してください
menu_item2.name = 'チョコケーキ'

# menu_item2のnameを出力してください
print(menu_item2.name)

# menu_item2のpriceに「400」を代入してください
menu_item2.price = 400

# menu_item2のpriceを出力してください
print(menu_item2.price)

#=====================================================================
# クラスの中では関数（メソッド）を定義できる
#　・メソッド：第1引数にselfを追加する必要がある
#　・インスタンス・メソッド()で、メソッドを呼び出せる
#
class MenuItem:
    # infoメソッドを定義してください
    def info(self):
        print('メニューの名前と値段が表示されます')


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

# menu_item1に対してinfoメソッドを呼び出してください
menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

# menu_item2に対してinfoメソッドを呼び出してください
menu_item2.info()
#=====================================================================
# インスタンスメソッドの第1引数に指定した self には、そのメソッドを呼び出した
# インスタンス自身が代入される
#
class MenuItem:
    def info(self):
        # 「○○: ¥□□」となるように出力してください
        print(self.name + ': ¥' + str(self.price))


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

menu_item1.info()

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

menu_item2.info()

#=====================================================================
# インタンスメソッド（戻り値）
class MenuItem:
    def info(self):
        # print()の中身を戻り値として返してください
        return self.name + ': ¥' + str(self.price)


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

# menu_item1.info()の値を出力してください
print(menu_item1.info())

menu_item2 = MenuItem()
menu_item2.name = 'チョコケーキ'
menu_item2.price = 400

# menu_item2.info()の値を出力してください
print(menu_item2.info())
