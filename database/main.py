from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker, relationship

from urllib.parse import quote_plus
from enum import Enum


class DatabaseType(Enum):
    POSTGRES = 0
    SQLITE = 1


# Создаем базовый класс для декларативного описания таблиц
class Base(DeclarativeBase):
    pass


class Database:
    def __init__(self):
        self.__engine = None
        self.__session = None

    @staticmethod
    def create_db_url(
            db_type: DatabaseType,
            username: str = None,
            password: str = None,
            host: str = None,
            port: int = None,
            database: str = None,
            **kwargs
    ) -> str:
        """
        Создает URL для подключения к базе данных (PostgreSQL или SQLite).

        :param db_type: Тип базы данных ("postgresql" или "sqlite").
        :param username: Имя пользователя базы данных (только для PostgreSQL).
        :param password: Пароль пользователя базы данных (только для PostgreSQL).
        :param host: Хост базы данных (только для PostgreSQL).
        :param port: Порт базы данных (только для PostgreSQL).
        :param database: Имя базы данных или путь к файлу SQLite.
        :param kwargs: Дополнительные параметры подключения.
        :return: Строка подключения к базе данных.
        """
        if db_type == DatabaseType.POSTGRES:
            if not all([username, password, host, port, database]):
                raise ValueError("Для PostgreSQL необходимо указать username, password, host, port и database.")
            password = quote_plus(password)
            url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

            if kwargs:
                params = "&".join([f"{key}={value}" for key, value in kwargs.items()])
                url += f"?{params}"

        elif db_type == DatabaseType.SQLITE:
            if not database:
                raise ValueError("Для SQLite необходимо указать database (путь к файлу).")
            url = f"sqlite:///{database}"

            if kwargs:
                print("Предупреждение: SQLite не поддерживает дополнительные параметры подключения.")

        else:
            raise ValueError(f"Неподдерживаемый тип базы данных: {db_type}. Используйте 'postgresql' или 'sqlite'.")

        return url

    def set_config(self, config):
        self.__engine = create_engine(config.set_db_url())
        self.__session = sessionmaker(bind=self.__engine)

    @property
    def session(self):
        return self.__session

    def create_all(self):
        Base.metadata.create_all(self.__engine)


db = Database()
