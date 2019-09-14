x = 7 * 10
y = 5 * 6

# xが70と等しい場合に「xは70です」と出力してください
if x == 70:
    print('xは70です')


# yが40と等しくない場合に「yは40ではありません」と出力してください
if y != 40:
    print('yは40ではありません')

#=====================================================================
# if
x = 10
# xが30より大きい場合に「xは30より大きいです」と出力してください
if x > 30:
    print('xは30より大きいです')


money = 500
apple_price = 200
# moneyの値がapple_priceの値以上の時、「りんごを買うことができます」と出力してください
if money >= apple_price:
    print('りんごを買うことができます')

#=====================================================================
# if, else
money = 100
apple_price = 200

if money >= apple_price:
    print('りんごを買うことができます')
# if文の条件に当てはまらない場合に「お金が足りません」と出力してください
else:
    print('お金が足りません')

#=====================================================================
# if, elif, else
money = 100
apple_price = 100

if money > apple_price:
    print('りんごを買うことができます')
# 変数の値が等しい場合に「りんごを買うことができますが所持金が0になります」と出力してください
elif money == apple_price:
    print('りんごを買うことができますが所持金が0になります')

else:
    print('お金が足りません')

#=====================================================================
# and, or, not
x = 20
# xが10以上30以下の場合に「xは10以上30以下です」と出力してください
if x >= 10 and x <= 30:
    print('xは10以上30以下です')

y = 60
# yが10未満または30より大きい場合に「yは10未満または30より大きいです」と出力してください
if y < 10 or y > 30:
    print('yは10未満または30より大きいです')

z = 55
# zが77ではない場合に「zは77ではありません」と出力してください
if not z == 77:
    print('zは77ではありません')

#=====================================================================
