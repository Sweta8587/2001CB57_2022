

# from datetime import datetime
# start_time = datetime.now()

# def attendance_report():
# ###Code

# from platform import python_version
# ver = python_version()

# if ver == "3.8.10":
#     print("Correct Version Installed")
# else:
#     print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")


# attendance_report()




# #This shall be the last lines of the code.
# end_time = datetime.now()
# print('Duration of Program Execution: {}'.format(end_time - start_time))

from datetime import datetime
start_time = datetime.now()

try:
    import os
    import pandas as pd
    from datetime import datetime, timedelta

except:
    print("install pandas,os & datatime and import it.")

else:
    classDates = []
   
    def preprocess(df):
        global classDates
        classes = set()
        for index in df.index:
            ts = df['Timestamp'][index]
            if '/' in ts:
                x = ts.split('/')
                date = x[0], month = x[1], year = x[2]
                if len(date) == 1:
                    date = '0'+date
                if len(month) == 1:
                    date = '0'+month
                ts = date + '-' + month + '-' + year
            dt = getTimestampValue(ts)
            if dt.weekday() in [0,3]:
                classes.add(dt.strftime("%d-%m-%Y"))
        classDates = list(classes)
        classDates.sort(key=lambda date: datetime.strptime(date, "%d-%m-%Y"))
        return df
    def getNameAndRoll(student):
        roll = student[:8]
        name = student[9:]
        return name, roll
   
    # return 1 for valid and 0 for invalid
    def getValidity(ts):
        time = ts.time()
        hour = time.hour
        minute = time.minute
        dayOfWeek = ts.weekday()
        if(dayOfWeek in [0, 3] and (hour == 14 or (hour == 15 and minute == 0))):
            return 1
        return 0
   
    def getDateFromTs(ts):
        return ts[:10]
   
    def getTimestampValue(ts_string):
        format_date = datetime.strptime(ts_string, '%d-%m-%Y %H:%M')
        return format_date
   
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)
           
    def getAllClassDates():
        classes = {}
        for single_date in classDates:
            classes[single_date] = 'A'
        return classes
   
    def getAllClassDuplicates():
        classes = {}
        for single_date in classDates:
            classes[single_date] = 0
        return classes
   
    def send_email(user, pwd, recipient):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication

        mail_content = '''
        Dear students,
        Please find the attached attendance report for CS384 class.
        Thank You
        '''

        sender_address = user
        sender_pass = pwd
        receiver_address = recipient
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'Attendance report for 2020 batch: CS384'
       
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'attendance_report_consolidated.csv'
       
        attach_file=MIMEApplication(open('Output/'+attach_file_name, 'rb').read())
        attach_file.add_header('Content-Disposition','attachment; filename="%s"' %attach_file_name)
        message.attach(attach_file)
