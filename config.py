from abc import abstractmethod

from database.main import Database, DatabaseType


class Configuration:
    def __init__(self):
        self.__db_url = self.set_db_url()

    @staticmethod
    @abstractmethod
    def set_db_url():
        pass

    @property
    def db_url(self):
        return self.__db_url


# временно prod & dev ничем не отличаются

class Production(Configuration):
    @staticmethod
    def set_db_url():
        return Database.create_db_url(
            db_type=DatabaseType.SQLITE,
            database='database_data/database.db'
        )


class Development(Configuration):
    @staticmethod
    def set_db_url():
        return Database.create_db_url(
            db_type=DatabaseType.SQLITE,
            database='database_data/database.db'
        )


conf = Production()
