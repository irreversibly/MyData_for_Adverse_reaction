from drug_crawler.read_data.excel_parser.model import *
from drug_crawler.crawler.crawlerbysite.model import *
from drug_crawler.drug_db.db_manager.model import *
from drug_crawler.drug_db.db_controller.model import *

if __name__ == "__main__":
    dbController = CrawlingDataCollector()
    mainCodeList = dbController.get_code_data()
    crawler = PublicDataPortal()
    fail_production_code = dbController.select_fail_caused_one()
    excelWriter = ExcelWriter()
    excelWriter.write_csv(fail_list=fail_production_code)
    # for i in range(1, 25609):
    #     select_result = dbController.select_public_or_fail(i)
    #     if select_result:
    #         print(i)
    #         try:
    #             crawlingData = crawler.operating(select_result[0])
    #             dbController.saveCrawlingData(i,crawlingData=crawlingData)
    #         except:
    #             dbController.saveFail(select_result[0],2)
    #


    # for mainCode in mainCodeList:
    #     try:
    #         crawlingData = crawler.operating(mainCode[1])
    #         dbController.saveCrawlingData(mainCode[0], crawlingData)
    #
    #     except Exception as ex:
    #         print(ex)
    #         dbController.saveFail(mainCode[0], 2)

    # for code in drug_template.read_data():
    #
    #
    # db_manager = DBManager()