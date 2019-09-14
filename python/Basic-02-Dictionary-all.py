# 商品を用意しよう
# 文字列のキーと数値の値を持つ辞書を作って、変数itemsに代入してください
items = {'apple':100, 'banana':200, 'orange':400}

# for文を用いて、辞書itemsのキーを1つずつ取り出していく繰り返し処理を作成してください
for item_name in items:
    # 「---------------------------------------------」を出力してください
    print('---------------------------------------------')
    # 「◯◯は1個△△円です」となるように出力してください
    print(item_name + 'は1個' + str(items[item_name])  + '円です')

#======================================================================
# 商品を購入しよう
items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    # inputを用いて入力を受け取り、変数input_countに代入してください
    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    # キーと変数input_countを用いて「購入する◯◯の個数は△△個です」となるように出力してください
    print('購入する' + item_name + 'の個数は' + input_count + '個です')

    # input_countを数値として変数countに代入してください
    count = int(input_count)

    # 変数total_priceに果物1個の値段と変数countを掛けた値を代入してください
    total_price = items[item_name] * count
    # 変数total_priceと型変換を用いて、「支払い金額は◯◯円です」となるように出力してください
    print('支払い金額は' + str(total_price) + '円です')

#======================================================================
# 条件分岐をしよう
# 変数moneyに数値1000を代入してください
money = 1000

items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    # 変数moneyを用いて「財布には◯◯円入っています」のように出力してください
    print('財布には' + str(money) + '円入っています')

    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')

    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')

    # moneyとtotal_priceの比較結果によって条件を分岐してください
    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')

#======================================================================
# 残金の計算を最後に加える

money = 1000
items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    print('財布には' + str(money) + '円入っています')
    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + item_name + 'の個数は' + input_count + '個です')

    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')

    if money >= total_price:
        print(item_name + 'を' + input_count + '個買いました')
        money -= total_price
        # moneyの値が0のとき条件を分岐してください
        if money == 0:
            print('財布が空になりました')
            break
            
    else:
        print('お金が足りません')
        print(item_name + 'を買えませんでした')
# 変数moneyと型変換を用いて、「残金は◯◯円です」となるように出力してください
print('残金は' + str(money) + '円です')
