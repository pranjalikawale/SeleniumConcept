import pytest
from utility.read_pdf_data import ReadPdf
from utility.constant import Constant

class TestForPdf():
    @pytest.fixture
    def read_pdf_object(self):
        self.constant_object=Constant()
        self.read_object=ReadPdf()
       
    def test_for_total_pages(self,read_pdf_object):
        assert  self.read_object.get_pdf_pages_count(self.constant_object.PATH_OF_PDF_FILE)==1
    
    def test_for_extract_data(self,read_pdf_object):
        page_number=0
        output=self.read_object.get_pdf_data(self.constant_object.PATH_OF_PDF_FILE,page_number)
        assert output[0]=="L"