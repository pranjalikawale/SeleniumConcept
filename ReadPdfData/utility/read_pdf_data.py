# importing required modules 
import PyPDF2 

class ReadPdf():

    def get_file_object(self,file_path):
        # creating a pdf file object 
        pdfFileObj = open(file_path, 'rb') 
        return  pdfFileObj

    def get_pdf_data(self,file_path,page_number):
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(self.get_file_object(file_path)) 
        # creating a page object 
        pageObj = pdfReader.getPage(page_number)  
        # extracting text from page 
        return pageObj.extractText()
    
    def get_pdf_pages_count(self,file_path):
        # creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(self.get_file_object(file_path)) 
        # printing number of pages in pdf file 
        return pdfReader.numPages
    