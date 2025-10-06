from payment_modes import PaymentMode
from payment_checkout import checkout

if __name__ == "__main__":
    amount = 143.20
    checkout(PaymentMode.PAYPAL, amount)
    checkout(PaymentMode.GOOGLEPAY, amount)
    checkout(PaymentMode.CREDITCARD, amount)
    checkout(PaymentMode.UNKNOWN, amount)
