from base_processor import PROCESSORS
from invalid_processor import InvalidProcessor

# Import all processors so they register themselves
import paypal_processor
import googlepay_processor
import creditcard_processor

def checkout(mode, amount: float):
    processor = PROCESSORS.get(mode, InvalidProcessor())
    processor.process(amount)
