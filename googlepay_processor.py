from base_processor import PaymentProcessor, register_processor
from payment_modes import PaymentMode

@register_processor(PaymentMode.GOOGLEPAY)
class GooglePayProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing GooglePay payment of ${amount:.2f}")
