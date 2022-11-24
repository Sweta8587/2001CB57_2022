

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
