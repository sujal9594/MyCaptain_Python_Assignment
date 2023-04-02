import csv

def write_into_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            writer.writerow(["Name", "Age", "Contact Number", "E-mail ID"])
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while condition:
        student_info = input("Enter student information for student #{} in the following format (Name Age Contact_Number E-mail_ID): ".format(student_num))
        
        
        student_info_list = student_info.split(' ')

        
        write_into_csv(student_info_list)

        choice = input("Enter (yes/no) if you want to enter information for another student: ")
        if choice.lower() == 'yes':
            condition = True
            student_num += 1
        else:
            condition = False
