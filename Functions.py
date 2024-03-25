#Import pandas
import pandas as pd

#import the file 
df = pd.read_excel('student_data.xlsx')

#create student class / intructor etc.
class Student:
    def __init__(self, barcode, id, time_in, email, student_class, instructor, name, role, department, institution, service, caseName):
        self.barcode = barcode
        self.id = id
        self.time_in = time_in
        self.email = email
        self.student_class = student_class
        self.instructor = instructor
        self.name = name
        self.role = role
        self.department = department
        self.institution = institution
        self.service = service
        self.caseName = caseName


#Create Function (Parameters=Student)
    #add a new row for a student, filling in data for each column specificied 
    #Validate Data before updating

#Read Function
    #Gets student data based off of name or barcode etc
    #iterate through columns, return the value inputted

#Update Function 
    #Validate Data before updating
    #Update existing student in excel

#Delete Function
    #Remove student based on certain value like barcode name etc.


