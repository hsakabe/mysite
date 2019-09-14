# from モジュール名 import クラス名　とすると
# 今までと同じようにクラスを用いる事ができる
#
# menu_item.pyからMenuItemクラスを読み込んでください
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')

#=====================================================================
# 各インスタンスを要素とするリストを変数へ代入
# そのリストに対してFor文で、インスタンス情報を出力できる
#
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

# 指定されたリストを変数menu_itemsに代入してください
menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# for文を作成してください
for menu_item in menu_items:
    print(menu_item.info())

#=====================================================================
# 繰り返し処理で番号をつける
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# 変数indexを定義し、数値の「0」を代入してください
index = 0

for menu_item in menu_items:
    # 「0. サンドイッチ: ¥500」となるように出力してください
    print(str(index) + '. ' + menu_item.info())

    # 変数indexに1を加えてください
    index += 1

#=====================================================================
# 入力を受け取るinput
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

# コンソールから入力を受け取り、変数orderに代入してください
order = int(input('メニューの番号を入力してください: '))

# 選択されたメニューを変数selected_menuに代入してください
selected_menu = menu_items[order]

# 「選択されたメニュー: 〇〇」と出力してください
print('選択されたメニュー: ' + selected_menu.name)

#=====================================================================
# 合計金額の計算
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('メニューの番号を入力してください: '))
selected_menu = menu_items[order]
print('選択されたメニュー: ' + selected_menu.name)

# コンソールから入力を受け取り、変数countに代入してください
count = int(input('個数を入力してください(3つ以上で1割引): '))

# get_total_priceメソッドを呼び出してください
result = selected_menu.get_total_price(count)

# 「合計は〇〇円です」となるように出力してください
print('合計は' + str(result) + '円です')
