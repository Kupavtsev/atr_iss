from app import db


class OHLC(db.Model):
    __tablename__ = 'ohlc_sber'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    session = db.Column(db.DateTime)
    open_price = db.Column(db.Float)
    high_price = db.Column(db.Float)
    low_price = db.Column(db.Float)
    close_price = db.Column(db.Float)
    voltoday = db.Column(db.Integer)

    def __init__(self, session, open_price, high_price, low_price, close_price, voltoday) -> None:
        self.session = session
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.voltoday = voltoday

    def __repr__(self):
        return f""