from abc import *
from ..save_model.model import *
from ..db_manager.model import *

class AbsDataCollector(metaclass=ABCMeta):
    def __init__(self):
        self._db_manager = DBManager()

    @abstractmethod
    def operating(self, data):
        pass

class CrawlingDataCollector(AbsDataCollector):
    def __init__(self):
        self._db_manager = DBManager()

    def operating(self, data):
        pass

    def get_code_data(self):
        return self._db_manager.select_all_main_code()

    def select_fail_caused_one(self):
        return self._db_manager.select_fail_caused_one()

    def select_public_or_fail(self, public_id):
        public = self._db_manager.select_public_portal(public_id)
        fail = self._db_manager.select_fail(public_id)
        result = None

        if (not public) and (not fail):
            result = self._db_manager.select_public_drug(public_id)

        return result

    def saveCrawlingData(self, codeId, crawlingData):
        crawlingModel = PublicCrawlingData(main_code_id=codeId , crawling_data=crawlingData)
        if crawlingModel.isFinishing():
            try:
                self._db_manager.insert_public_data(crawlingModel)
            except:
                self.saveFail(codeId = codeId, caused=3)
        else:
            self.saveFail(codeId=codeId, caused=1)

    def saveFail(self, codeId, caused):
        failData = Fail(codeId,caused)
        self._db_manager.insertFail(failData)



class AbsPreProcessingCollector(AbsDataCollector):
    def __init__(self):
        AbsDataCollector.__init__(self=self)
    @abstractmethod
    def operating(self, data):
        pass

class ExcelMainCodeCollector(AbsPreProcessingCollector):
    def __init__(self):
        AbsPreProcessingCollector.__init__(self=self)

    def operating(self, data):
        main_data = Main_Data(data)
        self._db_manager.save_main_code(main_data)

class ExcelPreProcessingCollector(AbsPreProcessingCollector):
    def __init__(self):
        AbsPreProcessingCollector.__init__(self=self)

    def operating(self, data):
        f_key = self._db_manager.select_main_code(data[0])
        data[0] = f_key[0]
        excel_data = Excel_Data(preprocessing_data=data)
        self._db_manager.insert_excel_data(excel_data)
        # del data[0]
        # data.append(f_key)
        # excel_data = Excel_Data(preprocessing_data=data)
        # self._db_manager.save_preprocessing_data(preprocessing_model=excel_data)

class ExcelBasicDrugCollector(AbsPreProcessingCollector):
    def __init__(self):
        AbsPreProcessingCollector.__init__(self=self)

    def operating(self, data):
        f_key = self._db_manager.select_basic_drug(data[0])
        data[0] = f_key[0]
        basic_data = BasicData(data)
        self._db_manager.save_basic_drug(basic_data)