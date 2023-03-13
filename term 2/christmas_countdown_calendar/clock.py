from settings import *

class Application(Frame):
    date = "12/25/2022"

    def initUI(self):
        # get access to the image
        self.event = "????????????"
        self.holiday_index = 0
        self.img_index = 0
        img = PhotoImage(file = path.join(img_folder_list[self.holiday_index],img_lists[self.holiday_index][self.img_index]))
        # create a lable that has the BG image
        self.bg = Label(self,image = img)
        self.bg.image = img
        # place background on the screen
        self.bg.place(x=0,y=0)


        self.event_selector = ttk.Combobox(self,textvariable="")
        self.event_selector["values"] = ("Valentines","Easter","Birthday","November","Christmas")
        self.event_selector["state"] = "readonly"
        self.event_selector.bind("<<ComboboxSelected>>",self.selectDate)
        self.event_selector.place(x=1500,y=900)

        self.monthdefaultVar = IntVar()
        self.monthdefaultVar.set(datetime.datetime.now().month)

        self.moSpinner = Spinbox(self,from_=1,to=12,width = 5,textvariable=self.monthdefaultVar,command=self.setDays)
        self.moSpinner.place(x=1650,y=900)

        days_in_month = 31
        x = self.moSpinner.get()
        if x in [4,6,9,11]:
            days_in_month = 30
        elif x == 2:
            days_in_month = 28
        else:
            days_in_month = 31

        self.daydefaultVar = IntVar()
        self.daydefaultVar.set(datetime.datetime.now().day)
        self.daySpinner = Spinbox(self, from_=1, to=days_in_month, width=5,textvariable=self.daydefaultVar)
        self.daySpinner.place(x=1700, y=900)
        current_year = datetime.datetime.now().year

        self.yeardefaultVar = IntVar()
        self.yeardefaultVar.set(datetime.datetime.now().year)
        self.yearSpinner = Spinbox(self, from_=current_year, to=current_year + 5, width=8,textvariable=self.yeardefaultVar)
        self.yearSpinner.place(x=1750, y=900)

        self.date = self.setDate()
        time = self.time_until(self.date)


        self.event_lbl = Label(self, text="Time until " + self.event, fg="teal", font=("helvetica", 58))
        self.event_lbl.place(x=100, y=100)
        Label(self, text="Days", fg="teal", font=("helvetica", 58)).place(x=200, y=200)
        Label(self, text="Hours", fg="teal", font=("helvetica", 58)).place(x=410, y=200)
        Label(self, text="Minutes", fg="teal", font=("helvetica", 58)).place(x=650, y=200)
        Label(self, text="Seconds", fg="teal", font=("helvetica", 58)).place(x=950, y=200)

        self.days_lbl = Label(self, text="0000", fg="teal", font=("helvetica", 58))
        self.days_lbl.place(x=200, y=300)
        self.hours_lbl = Label(self, text="0000", fg="teal", font=("helvetica", 58))
        self.hours_lbl.place(x=410, y=300)
        self.minutes_lbl = Label(self, text="0000", fg="teal", font=("helvetica", 58))
        self.minutes_lbl.place(x=650, y=300)
        self.sec_lbl = Label(self, text="0000", fg="teal", font=("helvetica", 58))
        self.sec_lbl.place(x=950, y=300)

        # rename and change command letter to set date
        self.change_image_bttn = Button(self,text = "Change",command = self.change)
        self.change_image_bttn.place(x=WIDTH/2,y=HEIGHT/2)

    def update(self):
        days = StringVar()
        days = self.time_until(self.date).days
        print(self.date)
        self.days_lbl.config(text = days)

        seconds = StringVar()
        total_seconds = self.time_until(self.date).seconds
        cursec = total_seconds%60
        seconds = cursec
        self.sec_lbl.config(text=seconds)
        print(seconds)

        minutes = StringVar()
        total_min = total_seconds// 60
        cur_min = total_min%60
        minutes = cur_min
        self.minutes_lbl.config(text=minutes)
        print(minutes)

        hours = StringVar()
        total_hours = total_min// 60
        cur_hour = total_hours%60
        hours = cur_hour
        self.hours_lbl.config(text=hours)
        print(hours)

        self.master.after(1,self.update)

    def setDays(self):
        days_in_month = 31
        x = self.moSpinner.get()
        if x in [4, 6, 9, 11]:
            days_in_month = 30
        elif x == 2:
            days_in_month = 28
        else:
            days_in_month = 31
        self.daySpinner.config["to"]=days_in_month

    def setDate(self):
        month = self.moSpinner.get()
        day = self.daySpinner.get()
        year = self.yearSpinner.get()
        return str(month)+"/"+str(day)+"/"+str(year)



    def change(self):
        ok = self.selectDate(self)

        if ok:
            self.img_index = random.randint(0,len(img_lists[self.holiday_index])-1)
            img = PhotoImage(file=path.join(img_folder_list[self.holiday_index],img_lists[self.holiday_index][self.img_index]))
            self.bg.configure(image=img)
            self.bg.image = img
        self.date = self.setDate()

    def selectDate(self,x):
        curDay = datetime.datetime.now().day
        curMonth = datetime.datetime.now().month
        curYear = datetime.datetime.now().year
        curDate = datetime.datetime.now()
        self.x = self.event_selector.get()

        if (self.x == "Christmas"):
            self.holiday_index = 4
            day = 25
            month = 12
            year=curYear
            date = datetime.datetime.strptime(str(month)+"/"+str(day)+"/"+str(curYear),"%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)

            return True
        elif self.x == "November":
            self.holiday_index = 3
            day = 1
            month = 11
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)
            return True
        elif self.x == "Easter":
            self.holiday_index = 1
            day = 9
            month = 4
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            self.daydefaultVar.set(day)
            self.monthdefaultVar.set(month)
            self.yeardefaultVar.set(year)
            return True
        elif self.x == "Birthday":
            self.holiday_index = 2
            return True
        elif self.x == "valentines":
            self.holiday_index = 0
            day = 25
            month = 14
            year = curYear
            date = datetime.datetime.strptime(str(month) + "/" + str(day) + "/" + str(curYear), "%m/%d/%Y")
            if curDate >= date:
                year += 1
            return True
        else:
            return True


    def time_until(self, date):

        date = datetime.datetime.strptime(date, "%m/%d/%Y")
        now = datetime.datetime.now()
        if date > now:
            time_until = date - now
            return time_until
        else:
            return now - now


    def __init__(self,master):
        super(Application, self).__init__(master)



        self.master.title(title)
        self.master.geometry(SCREEN_SIZE)
        self.master.configure(background = "green")
        self.initUI()
        # must be the last time in this method
        # This place this frame on the root window
        self.pack(fill=BOTH, expand=1)