from subprocess import Popen
import time
import os.path

processes = []
#name the logfile using current date
log = 'log/thrt_' + time.strftime('%d%m%y') + '.txt'

#make a directory named 'log'
if not os.path.exists('log'):
    os.makedirs('log')

#open file and set the mode to write, increment file name if file exists
num = 0
while(os.path.exists(log)):
    num = num + 1
    log = 'log/thrt_' + time.strftime('%d%m%y-') + str(num) +  '.txt'
    
#open file
file = open(log, 'w')

#add scripts to run in parallel
processes.append(Popen ('python searchBook.py WINDOWS firefox',stdout=file, stderr=file))
processes.append(Popen ('python searchBook.py WINDOWS chrome',stdout=file, stderr=file))


for subprocess in processes:
    subprocess.wait()