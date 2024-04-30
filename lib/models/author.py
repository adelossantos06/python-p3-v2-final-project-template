from models.__init__ import CURSOR, CONN

class Author:
    
    def__init__(self, name):
        self.name = name

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )