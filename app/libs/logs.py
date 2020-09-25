#log sistemi buradan düzenleniyor
from datetime import datetime
from filejobs import WriteFile,CreateFile,EditFile
LogFolder="/home/deniz/Masaüstü/opensource_projects/manuscript/logs/"
Time = datetime.now()
TimeLog=Time.strftime("%m/%d/%Y, %H:%M:%S")

def LogPrinter(AlertLevel,text):
 Log="time: {} Event :{} \n ".format(TimeLog,text)
 if AlertLevel == "Error":
   CreateFile(LogFolder+"Errors/Errors.txt")
   EditFile(LogFolder+"Errors/Errors.txt",Log)
 elif AlertLevel == "Info":
   CreateFile(LogFolder+"Info/Info.txt")
   EditFile(LogFolder+"Info/Info.txt",Log)
 else:
    CreateFile(LogFolder+"Info/Info.txt")
    EditFile(LogFolder+"Info/Info.txt",Log)



LogPrinter("Error","12321")