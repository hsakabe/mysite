# Foodクラスと、Drinkクラス
# 既にあるMenuItemクラスを元にして作成（共通部分をまとめる：効率的にコードを書く
# class 子クラス（親クラス）＜　継承（あるクラスを元にして新たなクラスを作成）
#
from menu_item import MenuItem

class Drink(MenuItem):

# __init__メソッドを定義してください
# __init__ メソッドも子クラスでオーバーライドできる

    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

 # infoメソッドを定義してください
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'
