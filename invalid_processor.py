from base_processor import PaymentProcessor

class InvalidProcessor(PaymentProcessor):
    def process(self, amount: float):
        print("Invalid payment mode selected!")
