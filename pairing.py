class PairsTrading(bt.Strategy):
    def __init__(self):
        self.spread = self.data0 - self.data1

    def next(se):
        if se.spreading > se.spreading.mean() + 2 * se.spreading.std():
            se.sell(data=se.data0)
            se.buy(data=se.data1)
        elif se.spreading < se.spreading.mean() - 2 * se.spreading.std():
            se.buy(data=se.data0)
            se.sell(data=se.data1)
