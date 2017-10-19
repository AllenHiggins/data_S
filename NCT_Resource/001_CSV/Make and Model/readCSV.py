import csv

file = raw_input("enter file name: ")

with open(file, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='|', quotechar='|')
    with open('somefile.txt', 'a') as the_file:
        count = 0
        for row in spamreader:
            count+=1
            if count >= 3:
                the_file.write(str(row) + '\n\n\n')
    the_file.close()

print("Task Completed!")
