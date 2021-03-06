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
            if i == 0 :
                sql += str(self._preprocessing_data[i]) + ","
            else:
                sql += "'" + self._preprocessing_data[i] +"', "
        sql += "'" + self._preprocessing_data[-1]+"'"
        return sql

    def set_f_key(self,f_key):
        self._preprocessing_data[0] = f_key


class PublicCrawlingData:
    def __init__(self, crawling_data, main_code_id):
        self.crawling_data = crawling_data
        self.main_code_id = main_code_id
        self._isFinished = True
        self.item_name = crawling_data["item_name"]
        if crawling_data["item_seq"] == -1:
            self._isFinished = False;

    def isFinishing(self):
        return self._isFinished

    def get_data(self):
        section = "(public_excel_id,"
        values = "(" + str(self.main_code_id) +","
        for key in self.crawling_data.keys():
            section += key+","
            if key == "item_seq":
                values += str(self.crawling_data[key]) +","
            elif key == "item_seq":
                values += str(self.crawling_data[key]) +","

            elif key == "class_no":
                if self.crawling_data[key]:
                    values += "'" + self.crawling_data[key] +"',"
                else:
                    values += "NULL,"
            elif key == "edi_code":
                if self.crawling_data[key]:
                    values += "'" + self.crawling_data[key] +"',"
                else:
                    values += "NULL,"
            else:
                values += "'" + self.crawling_data[key] +"' ,"
        section = section[:section.rindex(",")]
        values = values[:values.rindex(",")]
        section += ")"
        values += ")"

        return section + " VALUES" + values

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
    def __init__(self, main_code_id, caused):
        self.main_code_id = main_code_id
        self.caused = caused

    def get_data(self):
        return str(self.main_code_id) + " , " + str(self.caused)