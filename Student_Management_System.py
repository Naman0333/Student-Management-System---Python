#import Csv module
import csv
import os.path 

#create global variables
fields = ["Roll No.","Name","Age","Mobile No.","E-mail","Location"]
database = "database.csv"
file_exists = os.path.exists(database)


#Display Means  

def display_menu():
    print("-------------------------------------------")
    print("Welcome to Student Management System")
    print("-------------------------------------------")
    print("1. Add New Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Search Student")
    print("5. Delete Student")
    print("6. Quit")

#Create a Function for Add new Student Record.
def add_student():
    print("----------------------------------------")
    print("Add New Student Information!!!")
    print("----------------------------------------")

    global fields
    global database

    data=[]
    for field in fields:
        value = input(f"Enter the {field}:")
        data.append(value)

    with open("database.csv","a",newline="",encoding="utf-8") as wf:
        if not file_exists:
            writer = csv.DictWriter(wf,fieldnames=["Roll No.","Name","Age","Mobile No.","E-mail","Location"])
            writer.writeheader()
        else:
            writer = csv.writer(wf)
            writer.writerows([data])
    print("Your Data is Saved Sucessfully!!! ")
    print("Press any key for continue!!!")  
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
#Create a Function View Student Record.
def view_student():
    print("-----------------------------------")
    print("View Student Records!!!")
    print("-----------------------------------")

    global fields
    global database

    with open("database.csv","r",newline="",encoding="utf-8") as rf:
        read = csv.reader(rf)
        for field in fields:
            print(field, end="\t|")
        print("\n---------------------------------------------------------------")
        for row in read:
            for item in row:
                print(item,end="\t |")
            print("\n")
        input("Press any key for continue")

#Create a Function Update Student Record.
def update_student():
    print("--------------------------------------------")
    print("Update Student Information!!!")
    print("--------------------------------------------")

    global fields
    global database
    roll_no = input("Enter roll for updating Record")
    index_no = None
    updated_data =[]
    
    with open("database.csv","r",newline="",encoding="utf-8") as wf:
        reader = csv.reader(wf)
        counter = 0
        for row in reader:
            if len(row)>0:
                if roll_no == row[0]:
                    index_no = counter
                    print(f"Student Found as position : {index_no}")
                    data = []
                    for field in fields:
                        value = input(f"Enter {field}")
                        data.append(value)
                    updated_data.append(data)
                else:
                    updated_data.append(row)
                counter+=1

        if index_no is not None:
            with open("database.csv","w",newline="",encoding="utf-8") as wf:
                writer = csv.writer(wf)
                writer.writerows(updated_data)
        else:
            print("Roll No. not found in our database!!!")
        print("press any key for continue")

#Create a Function for Search Student Record.
def search_student():
    print("----------------------------------------")
    print("Search Student")
    print("----------------------------------------")

    global fields 
    global database
    roll_no = input("Enter the Roll No.")

    with open("database.csv","r",newline="",encoding="utf-8") as rf:
        reader = csv.reader(rf)
        for row in reader:
            if len(row)>0:
                if roll_no == row[0]:
                    print("---------------[Student Record Found]--------------")
                    print(f"Roll No. : {row[0]}")
                    print(f"Name     : {row[1]}")
                    print(f"Age      : {row[2]}")
                    print(f"Mobile No: {row[3]}")
                    print(f"E-mail   : {row[4]}")
                    print(f"Location : {row[5]}")
                    break
            else:
                print("----------------[Student Record Not Found]------------")
        print("Press any key for continue")

#Create a Function For Delete Record.
def delete_student():
    print("--------------------------------------")
    print("Delete Student Record!!!")
    print("--------------------------------------")

    global fields
    global database
    roll_no = input("Enter Roll No. for Delete Record!!!")
    updated_data = []
    student_index = False
    
    with open("database.csv","r",newline="",encoding="utf-8") as wf:
        reader = csv.reader(wf)
        counter=0
        for row in reader:
            if len(row)>0:
                if roll_no != row[0]:
                    updated_data.append(row)
                    counter+=1
                else:
                    student_index = True

    if student_index is True:
        with open("database.csv","w",newline="",encoding="utf-8") as wf:
            writer = csv.writer(wf)
            writer.writerows(updated_data)
        print(f"Student Record Deleted Successfully {roll_no}")
    else:
        print("Student Record Not Found!!!")
    input("Press any key for continue")

#infinity Loop for function Call.
while True:
    display_menu()
    choice = input("Enter your choice")
    if choice =="1":
        add_student()
    elif choice =="2":
        view_student()
    elif choice =="3":
        update_student()
    elif choice =="4":
        search_student()
    elif choice =="5":
        delete_student()
    else:
        break