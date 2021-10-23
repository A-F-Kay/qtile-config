from libqtile.widget import CryptoTicker


class MyCryptoTicker(CryptoTicker):

    def __init__(self, **config):
        super().__init__(**config)

    def parse(self, body):
        amount = float(body['data']['amount'])

        if self.amount_in_thousands:
            amount = amount / 1000

        return self.format.\
            format(crypto=self.crypto, symbol=self.symbol, amount=amount)
