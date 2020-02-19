# import csv module
import csv
fields =['name', 'branch', 'year', 'gpa']
# cvs-datei-name
filename='uni_records_2.csv'
dict_list=[{'name': 'Christoph', 'branch':'CEO', 'year':'2' , 'gpa':'9.1'},{'name': 'Joao', 'branch':'IT', 'year':'2' , 'gpa':'9.3'},{'name': 'Erik', 'branch':'MCE', 'year':'3' , 'gpa':'9.3'}]
 
# aus dictionary eine csv-datei erzeugen
with open(filename, 'w') as csvfile:
    # csv-dict-write-objekt
    writer=csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_list)