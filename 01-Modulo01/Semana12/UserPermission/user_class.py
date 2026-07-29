from abc import ABC, abstractmethod

class User(ABC):
    
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass