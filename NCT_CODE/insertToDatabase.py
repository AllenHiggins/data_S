import csv
import requests
def send():
    file = input("enter file name: ")
    year = str(file[:4])
    ifile  = open(file, "r")
    read = csv.reader(ifile)
    #wordList = []
    dict = {}
    count = 0
    to_remove = "[']'"
    for row in read :
        count+=1
        if count >=3 and count <8168:
            line = str(row)
            wordcounter = 0
            wordList = []
            for word in line.split(','):
                wordcounter+=1
                word = word.strip()
                tab = str.maketrans("", "", to_remove)
                word = word.translate(tab)
                wordList.append(word)
            dict['mmyf_make']=wordList[0]
            dict['mmyf_model']=wordList[1]
            a = wordList[2]
            dict['mmyf_yob']=int(a) 
            dict['mmyf_total']=wordList[3]
            dict['mmyf_pass']=wordList[4]
            dict['mmyf_percentagePass']=wordList[5]
            dict['mmyf_fail']=wordList[6]
            dict['mmyf_percentageFail']=wordList[7]
            dict['mmyf_vehicle_safetyEquipment']=wordList[8]
            dict['mmyf_percentagePass_vehicle_safetyEquipment']=wordList[9]
            dict['mmyf_light_electrical']=wordList[10]
            dict['mmyf_percentagePass_light_electrical']=wordList[11]
            dict['mmyf_steering_suspension']=wordList[12]
            dict['mmyf_percentagePass_steering_suspension']=wordList[13]
            dict['mmyf_breaking_equipment']=wordList[14]
            dict['mmyf_percentagePass_btreaking_equipment']=wordList[15]
            dict['mmyf_wheels_tyres']=wordList[16]
            dict['mmyf_percentagePass_wheels_tyres']=wordList[17]
            dict['mmyf_engine_noise_exhaust']=wordList[18]
            dict['mmyf_percentagePass_engine_noise_exhaust']=wordList[19]
            dict['mmyf_chassis_body']=wordList[20]
            dict['mmyf_percentagePass_chassis_body']=wordList[21]
            dict['mmyf_side_slip_test']=wordList[22]
            dict['mmyf_percentagePass_side_slip_test']=wordList[23]
            dict['mmyf_suspension_test']=wordList[24]
            dict['mmyf_percentagePass_suspension_test']=wordList[25]
            dict['mmyf_light_test']=wordList[26]
            dict['mmyf_percentagePass_light_test']=wordList[27]
            dict['mmyf_brake_test']=wordList[28]
            dict['mmyf_percentagePass_brake_test']=wordList[29]
            dict['mmyf_emission']=wordList[30]
            dict['mmyf_percentagePass_emission']=wordList[31]
            dict['mmyf_other']=wordList[32]
            dict['mmyf_percentagePass_other']=wordList[33]
            dict['mmyf_incomplete_test']=wordList[34]
            dict['mmyf_percentagePass_incomplete_test']=wordList[35]
            dict['mmyf_reportYear']=year
            
            #Cloud processing
            response =  requests.get('http://serversite.info:8080/NCT_API/nct/CAR', params=dict)
            #Local processing
            #response =  requests.get('http://localhost/loginapplication/nct/CAR', params=dict)
            #print(response.url)

    print("ReadyS")

def sendC():
    file = input("enter file name: ")
    year = str(file[:4])
    ifile  = open(file, "r")
    read = csv.reader(ifile)
    dict = {}
    count = 0
    to_remove = "%[']'"
    for row in read :
        count+=1
        if count >=4 and count <20:
            line = str(row)
            wordcounter = 0
            wordList = []
            for word in line.split(','):
                wordcounter+=1
                word = word.strip()
                tab = str.maketrans("", "", to_remove)
                word = word.translate(tab)
                wordList.append(word)
            dict['pfrtc_testCenter']=wordList[0]
            dict['pfrtc_vehiclePass']=wordList[1]
            dict['pfrtc_percentagePass']=wordList[2]
            dict['pfrtc_noIdNumber']=wordList[3]
            dict['pfrtc_percentageNoIdNumber']=wordList[4]
            dict['pfrtc_vehicleFail']=wordList[5]
            dict['pfrtc_percentageFail']=wordList[6]
            dict['pfrtc_failDangerous']=wordList[7]
            dict['pfrtc_perentageFailDangerous']=wordList[8]
            dict['pfrtc_totalVehiclesTested']=wordList[9]
            dict['pfrtc_reportYear']=year

            
            #Local processing
            print(requests.get('http://serversite.info:8080/NCT_API/nct/CTR', params=dict))
            #Cloud processing
            #response =  requests.get('http://localhost/loginapplication/nct/CTR', params=dict)
            #print(response.url)

    print("ReadyS")

