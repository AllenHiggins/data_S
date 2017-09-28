from tabula import convert_into
from PyPDF2 import PdfFileReader

#filename = raw_input('Enter PDF file Name to convert to CSV (ie; myFile):-->')
filename = 'Make_Model_data_2016' + '.pdf'
outputFileName = filename + '.csv'

try:
    reader = PdfFileReader(filename, 'r')
    totalPages = reader.getNumPages()
    convert_into(filename, outputFileName, output_format="csv", pages=range(1,totalPages))
except Exception as e:
     print('File not found. Please check name of file or if the file has been created')
