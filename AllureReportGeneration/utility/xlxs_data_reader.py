from utility.xls_util import XlsUtility
from utility.constant import Constant

class XlxsDataReader():
    
    def __init__(self):
        self.constant=Constant()

    def get_xlxs_data(self,sheet,row): 
            keyword=XlsUtility.read_data(sheet,row,self.constant.COLUMN_KEYWORD)
            locator=XlsUtility.read_data(sheet,row,self.constant.COLUMN_LOCATOR)
            locator_type=XlsUtility.read_data(sheet,row,self.constant.COLUMN_LOCATOR_TYPE)
            value=XlsUtility.read_data(sheet,row,self.constant.COLUMN_DATAVALUE)
            return keyword,locator,locator_type,value