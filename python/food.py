# Foodクラスと、Drinkクラス
# 既にあるMenuItemクラスを元にして作成（共通部分をまとめる：効率的にコードを書く
# class 子クラス（親クラス）＜　継承（あるクラスを元にして新たなクラスを作成）
#
from menu_item import MenuItem

class Food(MenuItem):

# __init__メソッドを定義してください
# __init__ メソッドも子クラスでオーバーライドできる

    def __init__(self, name, price, calorie):

# super()を用いて、親クラスの__init__()を呼び出してください
# メソッド内の重複をまとめる方法　＞　super()
# super().メソッド名() で、親クラス内に定義されたインタンスメソッドを利用可能

         super().__init__(name, price)
         self.calorie = calorie
         
# 以下の2行を削除してください
#       self.name = name
#       self.price = price



# infoメソッドを定義してください ＞　infoメソッドの改良（オーバライド）
# 親クラスにあるメソッドと同じ名前のメソッドを子クラスで定義すると
# メソッドを上書きできる　＞　オーバーライドと呼ぶ

    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'

# 子クラスでは、親クラスから引き継いだメソッド以外にも、独自にメソッドを追加できる
# 子クラスは「親クラス内で定義されているメソッド」と「独自に定義したメソッド」の両方が使える

    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')
