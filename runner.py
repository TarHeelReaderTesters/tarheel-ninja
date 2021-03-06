from subprocess import Popen
import time
import os.path
import sys






    
url = str(sys.argv[1])
script = str(sys.argv[2])

#name the logfile using current date
log = 'log/thrt_' + time.strftime('%d%m%y-00')

#make a directory named 'log'
if not os.path.exists('log'):
    os.makedirs('log')

#open file and set the mode to write, increment file name if file exists
num = 0
while(os.path.exists(log)):
    num = num + 1
    if num < 10:
        log = 'log/thrt_' + time.strftime('%d%m%y-0') + str(num)
    else:
        log = 'log/thrt_' + time.strftime('%d%m%y-') + str(num)

#open file
file = open(log, 'w')

processes = []
scriptNames = [ "login.py", "searchBook.py", "readBook.py", "mainMenu.py", "captureNewPics.py"] #,"bookContentReader.py","backgroundColor.py"]
#more scripts: "login.py", "searchBook.py","mainMenu.py","login.py","imageComparison.py"
#for script in scriptNames:
print 'Starting tests on script: ' + script
if script == "login.py":
#login.py has extra parameters
    script="login.py "+url+" tarheelreadertesters 40m4h99"
    url=""
#Mac scripts
processes.append(Popen ('python ' + script + ' ' + url +' MAC firefox',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python ' + script + ' ' + url +' MAC chrome',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python ' + script + ' ' + url +' MAC safari',stdout=file, stderr=file, shell=True))
#Windows scripts
processes.append(Popen ('python ' + script + ' ' + url +' WINDOWS iexplore 8',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python ' + script + ' ' + url +' WINDOWS iexplore 10',stdout=file, stderr=file, shell=True))


for subprocess in processes:
    subprocess.wait()

