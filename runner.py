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
processes.append(Popen ('python ssGrid.py MAC firefox http://tarheelreader.org/2013/11/18/tarheelreadertestbook/',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python ssGrid.py MAC chrome http://tarheelreader.org/2013/11/18/tarheelreadertestbook/',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python ssGrid.py MAC safari http://tarheelreader.org/2013/11/18/tarheelreadertestbook/',stdout=file, stderr=file, shell=True))

for subprocess in processes:
    subprocess.wait()