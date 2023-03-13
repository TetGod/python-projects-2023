from tkinter import *
import random
import datetime
from tkinter import ttk
from os import path

HEIGHT = 1080
WIDTH = 1920

SCREEN_SIZE = str(WIDTH)+"x"+str(HEIGHT)

title = "Christmas CountDown"

LOCATION = path.dirname(__file__)
img_folder = path.join(LOCATION,"imgs")
birthday_folder = path.join(img_folder,"birthday")
christmas_folder = path.join(img_folder,"christmas")
easter_folder = path.join(img_folder,"easter")
november_folder = path.join(img_folder,"november")
valentines_folder = path.join(img_folder,"valentines")

christmas_list = []
for i in range(5):
    christmas_list.append(str.format("christmas{}.png",i+1))

birthday_list = []
for i in range(5):
    birthday_list.append(str.format("birthday{}.png",i+1))

easter_list = []
for i in range(5):
    easter_list.append(str.format("easter{}.png",i+1))

november_list = []
for i in range(5):
    november_list.append(str.format("november{}.png",i+1))

valentines_list = []
for i in range(5):
    valentines_list.append(str.format("valentines{}.png",i+1))

img_folder_list = [valentines_folder,easter_folder,birthday_folder,november_folder,christmas_folder]
img_lists = [valentines_list,easter_list,birthday_list,november_list,christmas_list]