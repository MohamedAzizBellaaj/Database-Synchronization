from sqlalchemy import create_engine


class Database:
    __instance = None

    @classmethod
    def get_instance(cls, user, password, host, port, database):
        if not cls.__instance:
            cls.__instance = cls(user, password, host, port, database)
        return cls.__instance

    def __init__(self, user, password, host, port, database):
        self.engine = create_engine(
            f"mysql://{user}:{password}@{host}:{port}/{database}"
        )
