from abc import ABC, abstractmethod

#Abstract class for data sources (to use any type of data source,ex:csv),from various sources
class MainIngestor(ABC):

    @abstractmethod
    def read_msgs(self):
        pass
