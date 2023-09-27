from database import Database


class Store:
    def to_dict(self):
        ...

    def save(self):
        Database.insert(self.to_dict())
