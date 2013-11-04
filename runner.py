from subprocess import Popen

processes = []
test = 'amazonRC.py'
processes.append(Popen ('python amazonRC.py MAC firefox', shell=True))
processes.append(Popen ('python amazonRC.py MAC safari', shell=True))
processes.append(Popen ('python amazonRC.py MAC chrome', shell=True))
#processes.append(Popen ('python amazonRC.py MAC firefox', shell=True))
#processes.append(Popen ('python amazonRC.py MAC safari', shell=True))
#processes.append(Popen ('python amazonRC.py WINDOWS firefox', shell=True))
#processes.append(Popen ('python amazonRC.py WINDOWS iexplore 10', shell=True))
#processes.append(Popen ('python amazonRC.py WINDOWS chrome', shell=True))
processes.append(Popen ('python amazonRC.py WINDOWS iexplore 8', shell=True))
processes.append(Popen ('python amazonRC.py WINDOWS chrome', shell=True))
processes.append(Popen ('python amazonRC.py WINDOWS firefox', shell=True))

for process in processes:
    process.wait()