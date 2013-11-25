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
processes.append(Popen ('python captureNewPics.py MAC firefox',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureNewPics.py MAC chrome',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureNewPics.py MAC safari',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureBasePics.py MAC firefox',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureBasePics.py MAC chrome',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureBasePics.py MAC safari',stdout=file, stderr=file, shell=True))

processes.append(Popen ('python captureNewPics.py WINDOWS firefox',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureNewPics.py WINDOWS chrome',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureNewPics.py WINDOWS iexplore',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureBasePics.py WINDOWS firefox',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureBasePics.py WINDOWS chrome',stdout=file, stderr=file, shell=True))
processes.append(Popen ('python captureBasePics.py WINDOWS iexplore',stdout=file, stderr=file, shell=True))

for subprocess in processes:
    subprocess.wait()