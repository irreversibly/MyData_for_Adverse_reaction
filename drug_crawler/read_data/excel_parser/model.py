#-*-coding:utf-8-*-

from drug_crawler.read_data import model
import openpyxl


class DrugTemplateExcelParser(model.AbsReadData):

    def __init__(self, file_path):
        self._file_path = file_path

    def read_data(self):
        result = []
        try:
            excel_document = openpyxl.load_workbook(self._file_path)
            sheet = excel_document.get_sheet_by_name("20년7월1일_(25,608)")
            for i in range(2,25610):
                result.append(sheet.cell(row=i, column=2).value)
        except Exception as ex:
            print(ex)
        finally:
            excel_document.close()
        return result