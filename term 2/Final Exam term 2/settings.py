from tkinter import *
from os import path

HEIGHT = 420
WIDTH = 640
TITLE = "EXAMS"

SCREEN_SIZE = str(HEIGHT)+"x"+str(WIDTH)

file_name = "exams/ExampleTest.txt"

location = path.dirname(__file__)
exams_folder = path.join(location, "exams")
reports_folder = path.join(location,"Reports")
errorLogs = path.join(reports_folder,"ErrorLog")
reportCards = path.join(reports_folder,"reportCards")

test = path.join(exams_folder,file_name)
