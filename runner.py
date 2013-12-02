from subprocess import Popen
import time
import os.path

processes = []
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

#add scripts to run in parallel

def scripts():
    scriptNames = ["login.py", "mainMenu.py", "searchBook.py", "readSpecificBook.py", "readJapaneseContent.py", "captureNewPics.py"]
    for script in scriptNames:
            print 'Current script :' + script
            #Mac scripts
            processes.append(Popen ('python '+script+' MAC firefox',stdout=file, stderr=file, shell=True))
            processes.append(Popen ('python '+script+' MAC chrome',stdout=file, stderr=file, shell=True))
            processes.append(Popen ('python '+script+' MAC safari',stdout=file, stderr=file, shell=True))
            #Windows scripts
            processes.append(Popen ('python '+script+' WINDOWS iexplore 8',stdout=file, stderr=file, shell=True))
            processes.append(Popen ('python '+script+' WINDOWS iexplore 10',stdout=file, stderr=file, shell=True))
               

#login
#menu functionality
#search a book
#read a (specific) book
#read a Japanese book
#take the base screenshots (put this in a separate script)
#take the new screenshots
#do an image comparison between old and new


for subprocess in processes:
    subprocess.wait()
