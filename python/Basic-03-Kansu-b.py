# 名前を受け取る
def print_hand(hand, name='ゲスト'):
    print(name + 'は' + hand + 'を出しました')

print('じゃんけんをはじめます')

# inputを用いて入力を受け取り、変数player_nameに代入してください
player_name = input('名前を入力してください：')

# 変数player_nameの値によって関数print_handの呼び出し方を変更してください
if player_name == '':
    print_hand('グー')
else:
    print_hand('グー', player_name)

#========================================================================
# 出す手を選べるようにする
def print_hand(hand, name='ゲスト'):
    # 変数handsに、複数の文字列を要素に持つリストを代入してください
    hands = ['グー', 'チョキ', 'パー']

    # リストhandsを用いて、選択した手が出力されるように書き換えましょう
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
# 「何を出しますか？（0: グー, 1: チョキ, 2: パー）」と出力してください
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')

# inputを用いて入力を受け取り、数値に型変換してから変数player_handに代入してください
player_hand = int(input('数字で入力してください：'))

if player_name == '':
    # 第1引数を変数player_handに書き換えてください
    print_hand(player_hand)
else:
    # 第1引数を変数player_handに書き換えてください
    print_hand(player_hand, player_name)

#========================================================================
# 戻り値のある関数
# def 関数名():
#     retrun 戻り値
# ※returnは戻り値を呼び出し元に返すだけでなく、関数内の処理を終了させる性質も持っている
#
# 関数validateを定義してください
def validate(hand):
    # handの値によって条件分岐してください
    if hand < 0 or hand > 2:
        return False
    else:
        return True

def print_hand(hand, name='ゲスト'):
    hands = ['グー', 'チョキ', 'パー']
    print(name + 'は' + hands[hand] + 'を出しました')

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# 関数validateの戻り値がTrueの場合、以下のif~else文が実行されるようにしてください
if validate(player_hand):
    if player_name == '':
        print_hand(player_hand)
    else:
        print_hand(player_hand, player_name)
# 関数validateの戻り値がFalseの場合「正しい数値を入力してください」と出力してください
else:
    print('正しい数値を入力してください')
