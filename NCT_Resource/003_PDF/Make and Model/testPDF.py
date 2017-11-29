#Allen Higgins C00197373
#Zoltan Fuzesi C00197361
#Robert Scully C00196960



from tabula import convert_into
from PyPDF2 import PdfFileReader

#filename = input('Enter PDF file Name to convert to CSV (ie; myFile):-->')
filename = "2016.pdf"
outputFileName = "2016.csv"

try:
    reader = PdfFileReader(filename, 'r')
    totalPages = reader.getNumPages()
    convert_into(filename, outputFileName, output_format='csv', pages=range(1,2))
except Exception as e:
     print('File not found. Please check name of file or if the file has been created')
