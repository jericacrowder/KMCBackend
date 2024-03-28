#Import pandas library
import pandas as pd


#create Student Class
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
def create_student(df, barcode, id, time_in, email, student_class, instructor, name, role, department, institution, service, caseName):
    
    #Check if barcode is just numbers
    if not str(barcode).isdigit():
        return 
    
    #Create the new student using student class
    new_student = Student(barcode, id, time_in, email, student_class, instructor, name, role, department, institution, service, caseName)
    #Student Dictionary, this is used to append it to each column in the excel sheet.
    student_dict = new_student.__dict__

    #This creates the new student and appends it to the next available row in the excel file
    updated_df = df._append(student_dict, ignore_index=True)
    #Creates a new updated excel
    updated_df.to_excel('student_data_updated.xlsx', index=False)
    #returns the updated dataframe so you can continue making changes
    return updated_df


##Read Function
#print all names from column 'name'
def get_names(df): 
    print(df['name'])

#find student by id in the dataframe, print student info
def get_student(df, student_id):
    print("Searching for student...")
    student =  df.loc[df['id'] == student_id]
    if student.empty:
        print("No matches found")
    else:
        print(student)
    print("Search complete")

#Update Function 
    #Validate Data before updating
    #Update existing student in excel

#Delete Function
    #Remove student based on certain value like barcode name etc.

#Saves excel file as a CSV for easy importing to google sheets
def saveDailyCSV(df):
    # Exclude the first row
    df_to_save = df.iloc[1:].reset_index(drop=True)
    #Sets the file path 
    file_path = "C:\\Users\\pc\\Downloads\\daily_log.csv"
    #Creates a csv file with the excel file data
    df_to_save.to_csv(file_path, index=False)

#Saves a specific class's attendance as a pdf
def saveSpecificClassDaily(df, specified_class):
    #Sets the file path 
    file_path = "C:\\Users\\pc\\Downloads\\daily_class_log.pdf"
    #Sets the max number of students, change as needed
    max_students = 30
    #Creates a dataframe with only students from the specified class
    filtered_df = df[df["student_class"] == specified_class]
    
    # Create a figure and a single subplot
    fig, ax = plt.subplots(figsize=(11, len(filtered_df)))
    #Hide axes
    ax.axis("off")

    #Create the table with the filtered dataframe
    chart = ax.table(cellText = filtered_df.to_numpy(), colLabels = filtered_df.columns.tolist(), loc='center', cellLoc='center', rowLoc='center')

    # Adjust the font size of the table here
    chart.set_fontsize(10)
    chart.auto_set_column_width(col=list(range(len(filtered_df.columns))))

    # Save the figure as a PDF
    plt.savefig(file_path)

    # Clear the figure to free memory, especially important if calling this function multiple times
    plt.close(fig)
