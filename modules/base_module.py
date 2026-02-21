from abc import ABC, abstractmethod
from typing import Dict, Any
import logging

class BaseModule(ABC):
    @abstractmethod
    def process_message(self, message: Dict[str, Any]):
        pass
        
    def log_message(self, message: str, level: str = "INFO"):
        logging.getLogger(__name__).log(level, message)