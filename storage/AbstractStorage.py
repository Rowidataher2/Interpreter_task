from abc import ABC, abstractmethod

class BaseProducer(ABC):
    """
    Abstract base class for data sinks.
    """
    @abstractmethod
    def save_output(self, message, processed_value):
        pass
