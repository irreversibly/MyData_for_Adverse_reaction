import pymysql
from abc import *

class SingletonInstane:
  __instance = None

  @classmethod
  def __getInstance(cls):
    return cls.__instance

  @classmethod
  def instance(cls, *args, **kargs):
    cls.__instance = cls(*args, **kargs)
    cls.instance = cls.__getInstance
    return cls.__instance


class DBConnecter(SingletonInstane):

    def __init__(self):
        self.__host = ""
        self.__user = ""
        self.__password = ""
        self.__db = ""
        self.__charset = "utf8"

    def create_execute_query(self,query):
        conn = self._connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
        except Exception as ex:
            print(ex)

    def etc_execute_query(self,query,data):
        conn = self._connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query,data)
            conn.commit()
        except Exception as ex:
            print(ex)

    def _connect(self):
        return pymysql.connect(host=self.__host, user=self.__user, password=self.__password, db=self.__db, charset=self.__charset)


class AbsDBManager(metaclass=ABCMeta):

    def __init__(self):
        self._db_connect = DBConnecter.instance()

    @abstractmethod
    def create_db(self):
        pass


class DBManager(AbsDBManager):

    def __init__(self):
        AbsDBManager.__init__()

    def create_db(self):
        query = ""
        data = ""
