from drug_crawler.read_data.excel_parser.model import *
from drug_crawler.crawler.crawlerbysite.model import *
from drug_crawler.drug_db.db_manager.model import *
from drug_crawler.drug_db.db_controller.model import *

if __name__ == "__main__":
    dbController = CrawlingDataCollector()
    mainCodeList = dbController.select_fail_caused_one()
    excelWriter = ExcelWriter()
    excelWriter.write_csv(mainCodeList)
    # crawler = PublicDataPortal()
    # for fail in mainCodeList:
    #     # select_result = dbController.select_public_or_fail(i)
    #     if len(str(fail[1])) == 8:
    #         continue
    #     try:
    #         crawlingData = crawler.operating(fail[1])
    #         dbController.saveCrawlingData(fail[0], crawlingData=crawlingData)
    #     except Exception as ex:
    #         # print("status : 2")
    #         dbController.saveFail(fail[0], 2)
    # crawler.operating(53300270)

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