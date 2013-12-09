from subprocess import Popen
import time
import os.path
import sys


processes = []
url = str(sys.argv[1])

def scripts():
    global url
    script= "captureBasePics.py"
    print 'python '+script+' '+url+' MAC firefox'
    #Mac scripts
    processes.append(Popen ('python '+script+' '+url+' MAC firefox'))
    #processes.append(Popen ('python '+script+' '+url+' MAC chrome',stdout=file, stderr=file, shell=True))
    #processes.append(Popen ('python '+script+' '+url+' MAC safari',stdout=file, stderr=file, shell=True))
    #Windows scripts
    #processes.append(Popen ('python '+script+' '+url+' WINDOWS iexplore 8',stdout=file, stderr=file, shell=True))
    #processes.append(Popen ('python '+script+' '+url+' WINDOWS iexplore 10',stdout=file, stderr=file, shell=True))


    for subprocess in processes:
        subprocess.wait()

if __name__ == '__main__':
     scripts()
