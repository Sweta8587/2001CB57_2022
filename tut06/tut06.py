

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

        try:
            session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
            session.starttls() #enable security
            session.login(sender_address, sender_pass) #login with mail_id and password
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            print("successfully sent the mail")

        except:
            print('Failed to send the email!')
   
    def attendance_report():
        from platform import python_version
        ver = python_version()
   
        if ver == "3.8.10":
            print("Correct Version Installed")
        else:
            print("Please install 3.8.10. Instruction are present in the GitHub Repo/Webmail. Url: https://pastebin.com/nvibxmjw")
       
        d = {}
        try:
            attendance = pd.read_csv('input_attendance.csv')
            students = pd.read_csv('input_registered_students.csv')
        except :
            print("the input file does not exist at desired location")
       
        else:              
            attendance = preprocess(attendance)
            for index in students.index:
                d[students['Roll No'][index]] = {'Name': students['Name'][index], 'Date': getAllClassDates()}

            for index in attendance.index:
                ts = attendance['Timestamp'][index]
                name, roll = getNameAndRoll(attendance['Attendance'][index])
                date = getDateFromTs(ts)
                valid = getValidity(getTimestampValue(ts))
                old_value = (0, 0)
                if date in d[roll]:
                    old_value = d[roll][date]
           
                if valid:
                    d[roll][date] = (old_value[0] + 1, old_value[1])
                else:
                    d[roll][date] = (old_value[0], old_value[1] + 1)
           
           
            out3_keys = ['Roll', 'Name'] + classDates + ['Actual Lecture Taken', 'Total Real', '% Percentage']
            out3 = {}
           
            out4 = {}
           
            for k in out3_keys:
                out3[k] = []
                               
            for roll, v in d.items():
                total = 0
                valid = 0
                invalid = 0
                duplicates = 0
                absent = 0
               
                out2 = v['Date']
                out3['Roll'].append(roll)
                out3['Name'].append(v['Name'])
                out3['Actual Lecture Taken'].append(len(classDates))
                out4[roll] = getAllClassDuplicates()
               
                for index in classDates:
                    x = 0
                    y = 0
                   
                    if(index in v):
                        x = v[index][0]
                        y = v[index][1]
                   
                    if(x >= 1):
                        total += 1
       
                    if (x + y > 1):
                        duplicates += x + y
                   
                    if (x == 0):
                        absent += 1
                       
                    valid += x
                    invalid += y
                   
                    if(x >= 1):
                        out2[index] = 'P'
                    out3[index].append(out2[index])
                   
                    if(x + y > 1):
                        out4[roll][index] = x + y
                   
                out1 = {'Roll': roll,
                       'Name': v['Name'],
                       'Total Attendance Count': valid + invalid,
                       'Real': total,
                       'Duplicate': duplicates,
                       'Invalid': invalid,
                       'Absent': absent
                       }
                out3['Total Real'].append(total)
                out3['% Percentage'].append(round(total/len(classDates)*100, 2))
               
                df1 = pd.DataFrame(out1.items())
                df2 = pd.DataFrame(out2.items(), columns = ['Date', 'Attendance'])
               
                path = "Output"
                isOutputDirectoryExist = os.path.exists(path)
                if not isOutputDirectoryExist:
                    os.makedirs(path)
                df1 = df1.T
                df1.to_excel(r'Output\%s.xlsx'%roll)
               
                writer = pd.ExcelWriter(r'Output\%s.xlsx'%roll,engine='xlsxwriter')
                workbook=writer.book
                worksheet=workbook.add_worksheet(roll)
                writer.sheets[roll] = worksheet
       
                df1.to_excel(writer,sheet_name=roll,startrow=0 , startcol=0, header=None,index=False)
                df2.to_excel(writer,sheet_name=roll,startrow=df1.shape[0] + 2, startcol=0, index=False)
                writer.save()
           
            df3 = pd.DataFrame(out3, columns = out3_keys)
            df3.to_csv(r'Output\attendance_report_consolidated.csv')
           
            df4 = pd.DataFrame(out4)
            df4 = df4.T
            df4.to_csv(r'Output\attendance_report_duplicate.csv')
           
            user_input = input('Do you want to send email with attendance report (Y/N): ')
            if user_input.lower() == 'y':
                email = input('Please enter sender gmail account: ')
                password = input('Please enter sender app password (For knowing how to generate app password: https://stackoverflow.com/a/72553362/15394384): ')
                send_email(email, password, "cs3842022@gmail.com")
            elif user_input.lower() != 'n':
                print('Wrong input!')
           
    attendance_report()

#This shall be the last lines of the code.
end_time = datetime.now()
print('Duration of Program Execution: {}'.format(end_time - start_time))
