class Excel_Data:
    def __init__(self,preprocessing_data):
        self._preprocessing_data = preprocessing_data


    def get_data(self):
        data = str(self._preprocessing_data[0]) + ", " + self._preprocessing_data[1] + ", '" + self._preprocessing_data[2] +"' ," + " '" + self._preprocessing_data[3] +"'"
        # print(data)
        # data = str(self.main_ingr_code) +"," + str(self.production_code) + "," + str(self.company) + "," + str(self.name) + "," + str(self.ingredient) + "," + str(self.conc) + "," + str(self.condition) + "," + str(self.form) + "," + str(self.formulation) + "," + str(self.amt_num) + "," + str(self.amt_unit)
        return data

class BasicData:
    def __init__(self, preprocessing_data):
        self._preprocessing_data = preprocessing_data

    def get_data(self):
        sql = ""
        for i in range(len(self._preprocessing_data)-1):
            if i==0 :
                sql += str(self._preprocessing_data[i]) + ","
            else:
                sql += "'" + self._preprocessing_data[i] +"', "
        sql += "'" + self._preprocessing_data[-1]+"'"
        return sql

    def set_f_key(self,f_key):
        self._preprocessing_data[0] = f_key


class Public_Data_Portal:
    def __init__(self, crawling_data):
        self.excel_data_key = crawling_data["excel_data_key"]
        self.item_name = crawling_data["item_name"]
        self.item_seq = crawling_data["item_seq"]
        self.entp_name = crawling_data["entp_name"]
        self.class_no = crawling_data["class_no"]
        self.bar_code = crawling_data["bar_code"]
        self.material_name = crawling_data["material_name"]
        self.edi_code = crawling_data["edi_code"]
        self.main_item_ingr = crawling_data["main_item_ingr"]
        self.ingr_name = crawling_data["ingr_name"]
        self.nb_doc_data = crawling_data["nb_doc_data"]

class Main_Data:

    def __init__(self):
        self._id = -1
        self._main_ingr_code = ""
        self._date = None

    def __init__(self, main_ingr_code):
        self._id = -1
        self._main_ingr_code = main_ingr_code
        self._date = None

    def get_data(self):
        return self._main_ingr_code

class Fail:
    def __init__(self, production):
        self.production = production