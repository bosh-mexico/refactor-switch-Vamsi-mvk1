from base_processor import PaymentProcessor, register_processor
from payment_modes import PaymentMode

@register_processor(PaymentMode.PAYPAL)
class PayPalProcessor(PaymentProcessor):
    def process(self, amount: float):
        print(f"Processing PayPal payment of ${amount:.2f}")
