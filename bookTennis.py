from selenium import webdriver
import tkinter as tk
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pause
import time
import traceback
from tkinter import ttk
from tkcalendar import Calendar
import datetime
from tkinter import messagebox
from tennisAutomation import Tennis
from threading import *
import sys


import win32com.shell.shell as shell
import time
from elevate import elevate

elevate()
#
# def scheduleTask(bookDate):
#     elevate()
#     commands = r'schtasks /query /xml /tn "\test" > "C:\Users\sohum\OneDrive\Documents\Python Scripts\Selenium\tennis\task.xml'
#     shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)
#
#     time.sleep(1) # let file load
#     dateTime = f"{bookDate.split()[0]}T6:59:50"
#
#     import xml.etree.ElementTree as ET
#
#     with open('test.xml', 'r') as file:
#         filedata = file.read()
#
#     # Replace the target string
#     filedata = filedata.replace("UTF-16", "UTF-8")
#
#     # Write the file out again
#     with open('test.xml', 'w') as file:
#         file.write(filedata)
#
#     xmlTree = ET.parse("test.xml")
#     root = xmlTree.getroot()
#
#     element = root.find("{http://schemas.microsoft.com/windows/2004/02/mit/task}Triggers").find(
#         "{http://schemas.microsoft.com/windows/2004/02/mit/task}TimeTrigger").find(
#         "{http://schemas.microsoft.com/windows/2004/02/mit/task}StartBoundary")
#     element.text = dateTime
#
#     element = root.find("{http://schemas.microsoft.com/windows/2004/02/mit/task}Actions").find(
#         "{http://schemas.microsoft.com/windows/2004/02/mit/task}Exec").find(
#         "{http://schemas.microsoft.com/windows/2004/02/mit/task}Arguments")
#     element.text = bookDate
#
#     xmlTree.write("test.xml", encoding='UTF-8', xml_declaration=True)
#
#     with open('test.xml', 'r') as file:
#         filedata = file.read()
#
#     # Replace the target string
#     filedata = filedata.replace("UTF-8", "UTF-16")
#
#     # Write the file out again
#     with open('test.xml', 'w') as file:
#         file.write(filedata)
#
#     commands = r'schtasks /create /xml "C:\Users\sohum\OneDrive\Documents\Python Scripts\Selenium\tennis\task.xml" /tn "\test2"'
#     shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+commands)


# PATH = "C:\Program Fi les (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
#
# driver.get("https://canyoncreekhoa.tennisbookings.com/LoginX.aspx")

root = tk.Tk()
times = {"5 AM": 1, "5:30 AM": 2, "6 AM": 3, "6:30 AM": 4, "7 AM": 5, "7:30 AM": 6, "8 AM": 7, "8:30 AM": 8, "9 AM": 9, "9:30 AM": 10, "10 AM": 11, "10:30 AM": 12, "11 AM": 13, "11:30 AM": 14, "12 PM": 15, "12:30 PM": 16, "1 PM": 17, "1:30 PM": 18, "2 PM": 19, "2:30 PM": 20, "3 PM": 21, "3:30 PM": 22, "4 PM": 23, "4:30 PM": 24, "5 PM": 25, "5:30 PM": 26, "6 PM": 27, "6:30 PM": 28, "7 PM": 29, "7:30 PM": 30, "8 PM": 31, "8:30 PM": 32, "9 PM": 33, "9:30 PM": 34, "10 PM": 35}

window = tk.Frame(root, width=560, height=560, bg="white")
#window.grid(row=0, column=0)

def book():
    try:
        start = times[startTime.get()]
        end = times[endTime.get()] - 1

        print(f"end: {end}, start: {start}")
        bookDatestr = cal.get_date()
        bookDateArr = bookDatestr.split('/')
        bookDate = datetime.datetime(int("20" + bookDateArr[2]), int(bookDateArr[0]), int(bookDateArr[1]))
        date = datetime.datetime.now()
        difference = bookDate.day - date.day
        print(difference)
        if end > start and end - start <= 4 and int(bookDatestr[0:1]) - int(bookDatestr[0:1]) == 0 and difference > 3:
            commands = r'schtasks /query /xml /tn "\template" > "C:\Users\sohum\OneDrive\Documents\Python Scripts\Selenium\tennis\task.xml'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)

            time.sleep(1)  # let file load
            print(bookDate)
            dateTime = f"{str(bookDate - datetime.timedelta(3)).split(' ')[0]}T6:59:50"

            import xml.etree.ElementTree as ET

            with open('task.xml', 'r') as file:
                filedata = file.read()

            # Replace the target string
            filedata = filedata.replace("UTF-16", "UTF-8")

            # Write the file out again
            with open('task.xml', 'w') as file:
                file.write(filedata)

            xmlTree = ET.parse("task.xml")
            root = xmlTree.getroot()

            element = root.find("{http://schemas.microsoft.com/windows/2004/02/mit/task}Triggers").find(
                "{http://schemas.microsoft.com/windows/2004/02/mit/task}TimeTrigger").find(
                "{http://schemas.microsoft.com/windows/2004/02/mit/task}StartBoundary")
            element.text = dateTime

            element = root.find("{http://schemas.microsoft.com/windows/2004/02/mit/task}Actions").find(
                "{http://schemas.microsoft.com/windows/2004/02/mit/task}Exec").find(
                "{http://schemas.microsoft.com/windows/2004/02/mit/task}Arguments")
            dateOfBookDate = str(bookDate).split(" ")[0]
            element.text = f"{dateOfBookDate} {start} {end}"

            xmlTree.write("task.xml", encoding='UTF-8', xml_declaration=True)

            with open('task.xml', 'r') as file:
                filedata = file.read()

            # Replace the target string
            filedata = filedata.replace("UTF-8", "UTF-16")

            # Write the file out again
            with open('task.xml', 'w') as file:
                file.write(filedata)
            print("before")
            commands = rf'schtasks /create /xml "C:\Users\sohum\OneDrive\Documents\Python Scripts\Selenium\tennis\task.xml" /tn "\{dateOfBookDate} {start} {end}" /ru sohum /rp 908dad$SSlive'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + commands)
            print(bookDate)
        elif end > start and end - start <= 4:
            t1 = Tennis()
            t1.book(int(bookDateArr[0]), int(bookDateArr[1]), start, end - 1)
        else:
            messagebox.showinfo("Error", "End Time Must Be After Start Time And Max Booking Is 2 Hours")
    except:
        raise
        messagebox.showinfo("Error", "Invalid Input(s)")

def threadFunc():
    t1 = Thread(target=book)
    t1.start()

dateNow = datetime.datetime.now()
cal = Calendar(root, selectmode = 'day',
               year = dateNow.year, month = dateNow.month,
               day = dateNow.day)
cal.pack(pady = 20)

print(list(times.keys()))

selectedStartTime = tk.StringVar()
startTime = ttk.Combobox(root, textvariable=selectedStartTime)
startTime["values"] = list(times.keys())
#startTime["state"] = "readonly"
startTime.pack()

selectedEndTime = tk.StringVar()
endTime = ttk.Combobox(root, textvariable=selectedEndTime)
endTime["values"] = list(times.keys())
#startTime["state"] = "readonly"
endTime.pack()

bookButton = ttk.Button(root, text="Book", command=threadFunc)
bookButton.pack()

date = ttk.Label(root, text="")
date.pack(pady=20)


root.mainloop()
