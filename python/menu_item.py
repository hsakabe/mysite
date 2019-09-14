class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count

# countが3以上のとき、total_priceに0.9をかけてください
        if count >= 3:
            #total_price = tocal_price * 0.9
            total_price *= 0.9

# 整数と小数で計算した結果は、小数で出力される
# round(小数) ＞　小数を四捨五入した結果を取得

# total_priceを四捨五入して、returnしてください
        return round(total_price)
