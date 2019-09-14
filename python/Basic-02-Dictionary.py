# Dictionary Basic
# 変数fruitsに辞書を代入してください
fruits = {'apple':'りんご', 'banana':'バナナ'}

# 辞書fruitsのキー「banana」に対応する値を出力してください
print(fruits['banana'])

# 辞書fruitsを用いて、「appleは◯◯という意味です」となるように出力してください
print('appleは' + fruits['apple'] + 'という意味です')

#====================================================================
# Dictironay change & add
fruits = {'apple': 100, 'banana': 200, 'orange': 400}

# キー「banana」の値を数値「300」に更新してください
fruits['banana'] = 300

# キーが「grape」、値が数値の「500」の要素を辞書fruitsに追加してください
fruits['grape'] = 500

# fruitsの値を出力してください
print(fruits)

#====================================================================
# for 変数名 in 辞書:
fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}

# for文を用いて、辞書のキーを1つずつ取り出し、繰り返しの中で「◯◯は△△という意味です」と出力させてください
for fruit in fruits:
    print(fruit + 'は' + fruits[fruit] + 'という意味です')

#====================================================================
