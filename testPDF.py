from tabula import convert_into

convert_into('Make_Model_data_2016.pdf', "outPut.csv", output_format="csv", pages=range(1,5))
