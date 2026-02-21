import abc
from modules.base_module import BaseModule
from networking.protocol_manager import ProtocolManager

class Hub:
    def __init__(self):
        self.modules = {}
        self.protocol_manager = ProtocolManager(self)
        
    def register_module(self, module_id: str, module: BaseModule):
        if not isinstance(module, BaseModule):
            raise TypeError("Invalid module type")
        self.modules[module_id] = module
        
    def get_module(self, module_id: str) -> BaseModule:
        return self.modules.get(module_id)
        
    def handle_message(self, message):
        # Route message to appropriate module
        pass