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
        self.__host = "localhost"
        self.__user = "mdar_admin"
        self.__password = "mdar123"
        self.__db = "MDAR"
        self.__port = 3306
        self.__charset = "utf8"

    def create_execute_query(self,query):
        conn = self._connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
        except Exception as ex:
            print(ex)

    def insert_query(self,query):
        conn = self._connect()
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                conn.commit()
        except Exception as ex:
            conn.close()
            raise NameError("insert error")
        finally:
            conn.close()


    def select_query(self,query):
        conn = self._connect()
        result = -1
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            conn.close()
        return result

    def connect(self):
        return pymysql.connect(host=self.__host, port=self.__port, user=self.__user, password=self.__password, db=self.__db, charset=self.__charset)


class AbsDBManager(metaclass=ABCMeta):

    def __init__(self):
        self._db_connect = DBConnecter.instance()

    @abstractmethod
    def create_table(self, table_name):
        pass

    @abstractmethod
    def save_preprocessing_data(self,preprocessing_model):
        pass

    @abstractmethod
    def save_basic_drug(self, data):
        pass

    @abstractmethod
    def select_main_code(self,data):
        pass

    @abstractmethod
    def save_main_code(self,data):
        pass


class DBManager(AbsDBManager):

    def __init__(self):
        AbsDBManager.__init__(self = self)

    def create_table(self, table_name):
        sql = "CREATE TABLE " + table_name + " (" \
                                             "id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY," \
                                             "main_ingr_code VARCHAR(10) NOT NULL," \
                                             "production_code INT UNSIGNED NOT NULL," \
                                             "production_name TEXT NOT NULL," \
                                             "company VARCHAR(100) NOT NULL," \
                                             "name VARCHAR(30) NOT NULL," \
                                             "ingredient VARCHAR(30) NOT NULL," \
                                             "conc VARCHAR(15) NULL,"\
                                             "condition VARCHAR(20) NULL," \
                                             "form VARCHAR(2) NOT NULL," \
                                             "formulation VARCHAR(25) NOT NULL," \
                                             "amt_num FLOAT NOT NULL," \
                                             "amt_unit VARCHAR(10) NOT NULL);"
        self._db_connect.create_execute_query(sql)

    def save_preprocessing_data(self,preprocessing_model):
        sql = "INSERT INTO public_excel(main_ingr_code, production_code, company) VALUES("
        sql += preprocessing_model.get_data() + ");"
        self._db_connect.insert_query(query=sql)

    def save_basic_drug(self, data):
        conn = self._db_connect.connect()
        with conn.cursor() as cursor:
            try:
                data_sql = "INSERT INTO basic_drug(main_code_id, drug_name, ingredient, conc, drug_condition, form, formulation, amt_num, amt_unit) VALUES (" + data.get_data() + ");"
                cursor.execute(data_sql)
                conn.commit()
            except Exception as ex:
                print(ex)
            finally:
                conn.close()

    def insert_excel_data(self, data):
        conn = self._db_connect.connect()
        sql = "INSERT INTO public_excel (main_code_id ,production_code, production_name, company) VALUES (" + data.get_data() + ");"
        with conn.cursor() as cursor:
            try:
                cursor.execute(sql)
                conn.commit()
            except Exception as ex:
                print(ex)
            finally:
                conn.close()


    def select_main_code(self,main_ingr_code):
        sql = "SELECT id FROM main_code WHERE main_ingr_code = '" + main_ingr_code +"';"
        conn = self._db_connect.connect()
        result = -1
        with conn.cursor() as cursor:
            try:
                cursor.execute(query=sql)
                result = cursor.fetchone()
            except Exception as ex:
                print("expectation")
                print(ex)
            finally:
                conn.close()
        return result

    def save_main_code(self,data):
        conn = self._db_connect.connect()
        with conn.cursor() as cursor:
            try:
                main_model_sql = "INSERT INTO main_code(main_ingr_code) VALUES ('" + data.get_data() + "');"
                cursor.execute(main_model_sql)
                conn.commit()
            except Exception as ex:
                print(ex)
            finally:
                conn.close()
