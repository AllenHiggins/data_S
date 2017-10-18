#Allen Higgins C00197373
#Zoltan Fuzesi C00197361
#Robert Scully C00196960

from tabula import convert_into
from PyPDF2 import PdfFileReader

filename = raw_input('Enter PDF file Name to convert to CSV:--> ')

try:
    reader = PdfFileReader(filename, 'r')
    totalPages = reader.getNumPages()
    outputFileName = filename[0:-4] + '.csv'
    convert_into(filename, outputFileName, output_format="csv", pages=range(2,totalPages))
except Exception as e:
     print('File not found. Please check name of file or if the file has been created')
