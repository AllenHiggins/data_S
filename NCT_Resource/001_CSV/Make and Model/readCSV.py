import csv
from decimal import Decimal

#file = raw_input("enter file name: ")
file = '2013.csv'
year = str(file[:4])

with open(file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    count = 0
    wordCout = 0
    wordList=[]
    for row in spamreader:
        count+=1
        if count >= 3:
            line = str(row[0])
            for word in line.split(','):
                wordList.append(word)
            #Appened extra col at end call API Here
            apiCall = 'http://localhost/data/nct?mmyf_make='+wordList[0]+'&mmyf_model='+wordList[1]+'&mmyf_yob='+wordList[2]+'&mmyf_total=' + wordList[3] + '&mmyf_pass=' + wordList[4] + '&mmyf_percentagePass=' + wordList[5] + '&mmyf_fail=' + wordList[6] + '&mmyf_percentageFail=' + wordList[7] + '&mmyf_vehicle_safetyEquipment=' + wordList[8] + '&mmyf_percentagePass_vehicle_safetyEquipment=' + wordList[9] + '&mmyf_light_electrical=' + wordList[10] + '&mmyf_percentagePass_light_electrical=' + wordList[11] + '&mmyf_steering_suspension=' + wordList[12] + '&mmyf_percentagePass_steering_suspension=' + wordList[13] + '&mmyf_breaking_equipment=' + wordList[14] + '&mmyf_percentagePass_btreaking_equipment=' + wordList[15] + '&mmyf_wheels_tyres=' + wordList[16] + '&mmyf_percentagePass_wheels_tyres=' + wordList[17] + '&mmyf_engine_noise_exhaust=' + wordList[18] + '&mmyf_percentagePass_engine_noise_exhaust=' + wordList[19] + '&mmyf_chassis_body=' + wordList[20] + '&mmyf_percentagePass_chassis_body=' + wordList[21] + '&mmyf_side_slip_test=' + wordList[22] + '&mmyf_percentagePass_side_slip_test=' + wordList[23] + '&mmyf_suspension_test=' + wordList[24] + '&mmyf_percentagePass_suspension_test=' + wordList[25] + '&mmyf_light_test=fail=' + wordList[26] + '&mmyf_percentagePass_light_test=' + wordList[27] + '&mmyf_brake_test=' + wordList[28] + '&mmyf_percentagePass_brake_test=' + wordList[29] + '&mmyf_emission=' + wordList[30] + '&mmyf_percentagePass_emission=' + wordList[31] + '&mmyf_other=' + wordList[32] + '&mmyf_percentagePass_other=' + wordList[33] + '&mmyf_incomplete_test=' + wordList[34] + '&mmyf_percentagePass_incomplete_test=' + wordList[35] + '&mmyf_reportYear=' + year


            print apiCall
            raw_input()
