from drug_crawler.read_data.excel_parser.model import *
from drug_crawler.crawler.crawlerbysite.model import *
from drug_crawler.drug_db.db_manager.model import *
from drug_crawler.drug_db.db_controller.model import *

if __name__ == "__main__":
    drug_template = DrugTemplateExcelParser("../../drug_template.xlsx")
    basic_collector = ExcelPreProcessingCollector()
    basic_drug_list = drug_template.read_data()
    for i in range(0,len(basic_drug_list)):
        print(basic_drug_list[i])
        basic_collector.operating(data=basic_drug_list[i])
    # for code in drug_template.read_data():
    #
    #
    # db_manager = DBManager()