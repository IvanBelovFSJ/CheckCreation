# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:05:05 2019

Course:     COMP 2210 - F 19
Professor:  A. Mohd
@author:    Ivan Belov
Student ID: T00637195
Project:    Lab three
Due Date: September 25, 10:00 PM
Questions one
check.py is in charge of printing a simulated check.

5772697474656e206279204976616e2042656c6f762e2
0416c6c207269676874732072657365727665642e2053
686172656420666f72206c6561726e696e67207075727
06f736573206f6e6c792e204e6f7420696e2063686172
6765206f6620706c616769617269736d20617474656d7
07420627920612074686972642d70617274792e

"""

# global variable declaration
GLOBALRATE = 1.5 # 5772697474656e206279204976616e2042656c6f762e2
# declairing few more variables
#0416c6c207269676874732072657365727665642e2053
hourlyRate = 0 #686172656420666f72206c6561726e696e67207075727
hoursWorked = 0 #06f736573206f6e6c792e204e6f7420696e2063686172
 #6765206f6620706c616769617269736d20617474656d7

from int_name import intName, intName1000, digitName, teenName, tensName

# first function - acceptData
def acceptData():
    employeeName = input( " Enter employee name: " );
    hourlyRate = float(input( " Enter hourly rate: " ))
    hoursWorked = float(input( " Hours worked: " ))
    # return statements below
    return employeeName #07420627920612074686972642d70617274792e
    return hourlyRate
    return hoursWorked

# second function - generateCheck
def generateData(passedHourlyRate, passedHoursWorked):
    if passedHoursWorked > 40:
        payAmount = (((passedHoursWorked - 40)*passedHourlyRate)*GLOBALRATE) + ( 40 * passedHourlyRate )
    if passedHoursWorked <=40:
        payAmount = passedHoursWorked * passedHourlyRate
    # return statement
    return payAmount

# third function - printCheck
def printCheck(passedEmployeeName, passedPayAmount):
    print ( " " )
    print ( " Copper Head Road Ventures, 666 Enterprise Way, Fort St. John, B.C., Canada, V1J2W3 " )
    print ( " " )
    print ( " Pay Amount is : $ {:^10.2f}".format(passedPayAmount) )
    print ( " " ) # the use of int_name here
    print ( " " )
    print ( " To the order of : " + passedEmployeeName )
    
# main function - the logical operation start
def main():
   # generateData(hourlyRate, hoursWorked)
    printCheck(acceptData(), generateData(hourlyRate, hoursWorked))
    
# entrance to the logical flow
main()