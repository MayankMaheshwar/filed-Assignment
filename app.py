from flask import Flask, request, render_template, redirect, url_for
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)


@app.route('/')
def home():

    return render_template('payment.html')


@app.route('/processPayment', methods=['GET', 'POST'])
def hello():
    req = request.form

    amount = req.get('amount')
    print(type(amount))
    amount = int(amount)
    if amount <= 20:
        return 'use CheapPaymentGateway'
    elif amount > 20 and amount <= 500:
        return 'use ExpensivePaymentGateway'
    else:
        return redirect(url_for('hie'))


@app.route('/expensive')
@limiter.limit('3 per day')
def hie():
    return 'use PremiumPaymentGateway'


if __name__ == '__main__':
    app.run()
