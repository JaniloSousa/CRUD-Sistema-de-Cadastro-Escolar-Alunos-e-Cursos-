import sqlalchemy as db
from sqlalchemy.orm import sessionmaker

class ConnectionHandler:
    def __init__(self):
        self.__connectionString = 'mysql+pymysql://root:@localhost:3306/escola'
        self.__engine = self.__createDatabaseEngine()
        self.session = None


    def __createDatabaseEngine(self):
        engine = db.create_engine(self.__connectionString)
        return engine
        

    def __enter__(self):
        Session = sessionmaker(bind=self.__engine)
        self.session = Session()
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()