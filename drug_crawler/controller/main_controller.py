from drug_crawler.read_data.excel_parser.model import *
from drug_crawler.crawler.crawlerbysite.model import *
from drug_crawler.drug_db.db_manager.model import *
from drug_crawler.drug_db.db_controller.model import *
import time
if __name__ == "__main__":
    dbProductionController = ProductionCodeController()
    nbdocdata = NbDocDataParser()
    for code in dbProductionController.select_working():
        try:
            data = nbdocdata.operating(code[0])
            dbProductionController.update_nb_doc_data(data=data, id=code[0])
        except Exception as ex:
            print(ex)
    # dbProductionController.select_working()
    # nb_doc = NbDocDataParser()
    # production_code_list = {}
    # production_crawler = ProductionCode()
    # for code in dbProductionController.select_production_code():
    #     production_code_list[code[0]] = 1
    #
    # for code in dbProductionController.select_working():
    #     del production_code_list[code[0]]
    #
    # for code in production_code_list.keys():
    #     try:
    #         data = production_crawler.operating(code)
    #         data["ITEM_SEQ"] = code
    #         dbProductionController.operating(data=data)
    #     except NotFoundCrawlingException as ex:
    #         dbProductionController.save_fail(code, str(ex))
    #     except ConnectError as ex:
    #         dbProductionController.save_fail(code,str(ex))
    #     except DBSQLError as ex:
    #         dbProductionController.save_fail(code,str(ex))
    #     except Exception as ex:
    #         dbProductionController.save_fail(code,str(ex))

    # for production in productionCodeList:
    #     try:
    #         data = productionCrawler.operating(production[0])
    #         dbProductionCode.operating(data=data)
    #     except NotFoundCode:
    #         dbProductionCode.save_fail(production[0])
    #     except Exception as ex:
    #         print(ex)
    # dbController = CrawlingDataCollector()
    # mainCodeList = dbController.select_fail_caused_one()
    # excelWriter = ExcelWriter()
    # excelWriter.write_csv(mainCodeList)
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