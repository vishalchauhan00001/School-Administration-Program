#student administration tool
from typing import ClassVar
import csv 

def write_csv_file(info_list):
    with open('student_info.csv','a',newline='')as csv_file:
    writer = csv.writer(csv_file)
    
    if csv_file.tell == 0:
    writer.writerow("Name","Age","Contact_Number", "Email_Id")

    if__name__ == '__main__':
    condition = True
    student_num = 1

    while(condition) :
        student_info = input("Enter some students information in the following format (Name Age Contact_Number Email_Id): ")
        print("Enter information:" + student_info)

    #split
    student_info_list = student_info.split(' ')
    print("Enter split up information: " + str(student_info_list))
    print("\n The entered information is-\nName:{}\n Age:{}\n Contact_Number:{}\n E-mail_Id:{}\n"
    .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
    
    condition_check = input("Enter (yes/no) if you want to enter information for another student: ")

    if condition_check=="yes" :
    condition = True 
    student_num = student_num +1

    elif condition_check == "no" :
        condition = False
    print("/nplease re-enter the values!")