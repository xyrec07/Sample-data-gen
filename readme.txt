--------------
DATA GENERATOR
--------------

*Open emp and run em.exe
*(For GUI open emp(GUI) and run empl.exe)
*Python file is with the .exe  

-------------------------------------------------------------------------
This program generate a .csv file containing random generated data for the
 entered number of people.
-------------------------------------------------------------------------

NOTE- .csv file is generated in the same folder as empl.

The data include-
[emp_id, emp_firstname, emp_lastname, dob, gender, hire_date, to_date] 

~dob is such that the age according to the current date is atlest 20yrs.
~hire_date is between (dob + 20yrs) to current date.
~to_date (leaving date) is between hire and current date but the chance that a person left is 10%

-----------------------------------------------------
Modules used [pandas, numpy, datetime, name, tkinter]
-----------------------------------------------------

---------------
Harshit Chuahan
---------------
