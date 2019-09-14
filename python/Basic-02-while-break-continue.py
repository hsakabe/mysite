# while 条件式:
x = 10

# while文を用いて、「変数xが0より大きい」間、繰り返される繰り返し処理を作ってください
while x > 0:
    # 変数xを出力してください
    print(x)
    # 変数xから1引いてください
    x -= 1

#==========================================================================
# break > 繰り返し処理を終了
numbers = [765, 921, 777, 256]
for number in numbers:
    print(number)
    # 変数numberが777のとき「777が見つかったので処理を終了します」と出力した後、処理を終了させてください
    if number == 777:
        print('777が見つかったので処理を終了します')
        break

#==========================================================================
# continueはその周の処理だけをスキップ
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    # 変数numberの値が3の倍数のとき、繰り返し処理をスキップしてください
    if number % 3 == 0:
        continue
    print(number)

#==========================================================================