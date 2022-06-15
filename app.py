from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from get_sber import get_ohlc_sber


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class OHLC_Model(db.Model):
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

@app.route('/sber', methods=['POST', 'GET'])
def handle_ohlc(data = get_ohlc_sber()):
    if request.method == 'GET':
        if bool(data):
            # print('GET method: ', data)
            # prev_session = OHLC_Model.query.all()
            # print('prev_session: ', prev_session.session)
            # We getting prev session record by last ID
            prev_session = OHLC_Model.query.order_by(OHLC_Model.id.desc()).first().session
            # print('prev_session: ', prev_session)
            # print('prev_session: ', prev_session.session)

            new_session = OHLC_Model(
                session=data['SYSTIME'],
                open_price=data['OPEN'],
                high_price=data['HIGH'],
                low_price=data['LOW'],
                close_price=data['LAST'],
                voltoday=data['VOLTODAY'],
            )
            
            # We need to delete prev session if its the same as in new request
            # if prev_session.session
            
            print('new_session: ', new_session.session)
            db.session.add(new_session)
            db.session.commit()
            return {"message": f"day {new_session.session} has been created successfully."}
            # return print(f"day {new_session.session} has been created successfully.")
        else:
            return {"error": "The request payload is not in valid format"}
            # return print("error: The request payload is not in valid format")


if __name__ == '__main__':
    app.run()
