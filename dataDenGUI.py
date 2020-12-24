import names
import datetime
import random
import pandas as pd
import numpy as np
import tkinter as tk


def random_date_generator():
    start_date = datetime.date(1975, 1, 1)
    # 20 yrs = 7300 days
    end_date = datetime.date.today() - datetime.timedelta(days=7300)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date


def leaving_date_generator(random_hire_date):
    leaving_probability = random.randint(0, 100)
    if leaving_probability > 90:
        days_worked = random.randint(
            1, (datetime.date.today() - random_hire_date).days)
        dol = random_hire_date + datetime.timedelta(days=days_worked)
        return dol

    else:
        dol = None
        return dol


def random_people_generator(num):
    emp_id = []
    first_name = []
    last_name = []
    gender = []
    dept = []
    dob = []
    hire_date = []
    to_date = []
    dept_list = ['Accounts_and_Finance', 'HR', 'Sales_and_Marketing',
                 'Research_and_development', 'Product_development']
    for i in range(0, num):
        random_gender = random.choice(['male', 'female'])
        random_firstname = names.get_first_name(gender=random_gender)
        random_lastname = names.get_last_name()
        random_dept = random.choice(dept_list)
        random_dob = random_date_generator()

        date_at_age_20 = random_dob + datetime.timedelta(days=7300)
        hire_days = random.randint(
            1, ((datetime.date.today() - date_at_age_20).days))
        random_hire_date = random_dob + \
            datetime.timedelta(days=(7300 + hire_days))
        random_to_date = leaving_date_generator(random_hire_date)

        emp_id.append(1001 + i)
        first_name.append(random_firstname)
        last_name.append(random_lastname)
        gender.append(random_gender)
        dept.append(random_dept)
        dob.append(random_dob)
        hire_date.append(random_hire_date)
        to_date.append(random_to_date)
    return emp_id, first_name, last_name, dob, gender, dept, hire_date, to_date


root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
no_var = tk.StringVar()
name_var = tk.StringVar()


def submit():
    data = {}
    data['emp_id'], data['first_name'], data['last_name'], data['dob'], data[
        'gender'], data['dept'], data['hire_date'], data['to_date'], = random_people_generator(int(no_entry.get()))

    employee = pd.DataFrame(data)
    # print(employee)
    file_name = name_entry.get() + '.csv'
    employee.to_csv(file_name, index=False)


# text using widget Label
ask_no_label = tk.Label(root, text='How many rows do you want:',
                        font=('calibre',
                              10, 'bold'))

# creating a entry for input
# Using widget Entry
no_entry = tk.Entry(root,
                    textvariable=no_var, font=('calibre', 10, 'normal'))

# text using widget Label
ask_name_label = tk.Label(root, text='Name of the file(don\'t include .csv):',
                          font=('calibre',
                                10, 'bold'))

# creating a entry for input
# Using widget Entry
name_entry = tk.Entry(root,
                      textvariable=name_var, font=('calibre', 10, 'normal'))

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit',
                    command=submit)


ask_no_label.grid(row=0, column=0)
no_entry.grid(row=0, column=1)
ask_name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)


root.mainloop()

# BY HARSHIT CHAUHAN
