from subprocess import Popen
import time
import os.path
import sys

processes = []

if(len(sys.argv)!=2):
        print "Invalid number of parameters!"
        print "Format is: %s <url>" % (sys.argv[0],)
	sys.exit(1)

url = str(sys.argv[1])



#add scripts to run in parallel

def scripts():
    global processes, url
    scriptNames = [ "captureBasePics.py"]
    for script in scriptNames:
            #Mac scripts
            processes.append(Popen ('python '+script+' '+url+' MAC firefox', shell=True))
            processes.append(Popen ('python '+script+' '+url+' MAC chrome',shell=True))
            processes.append(Popen ('python '+script+' '+url+' MAC safari', shell=True))
            #Windows scripts
            processes.append(Popen ('python '+script+' '+url+' WINDOWS iexplore 8',shell=True))
            processes.append(Popen ('python '+script+' '+url+' WINDOWS iexplore 10',shell=True))
            processes.append(Popen ('python '+script+' '+url+' WINDOWS firefox', shell=True))
            processes.append(Popen ('python '+script+' '+url+' WINDOWS chrome',shell=True))

            for subprocess in processes:
                    subprocess.wait()
            processes = []

if __name__ == '__main__':
    scripts()
