from abc import ABC, abstractmethod

# Global registry
PROCESSORS = {}

def register_processor(mode):
    """Decorator to auto-register processors"""
    def decorator(cls):
        PROCESSORS[mode] = cls()
        return cls
    return decorator


class PaymentProcessor(ABC):
    @abstractmethod
    def process(self, amount: float):
        pass
