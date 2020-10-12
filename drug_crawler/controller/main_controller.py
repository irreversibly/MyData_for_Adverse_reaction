from drug_crawler.read_data.excel_parser.model import *
from drug_crawler.crawler.crawlerbysite.model import *
if __name__ == "__main__":
    drug_template = DrugTemplateExcelParser("../../drug_template.xlsx")
    code_list = "643507540"
    print(PublicDataPortal().operating(code_list))
    # for code in drug_template.read_data()