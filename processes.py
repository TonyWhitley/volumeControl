# pylint: skip-file
# type: ignore
import psutil

class Processes:
	def __init__(self):
		self.get_processes()
	def get_processes(self):
		self.listOfProcessNames = list()
		# Iterate over all running processes
		for proc in psutil.process_iter():
		   # Get process detail as dictionary
		   pInfoDict = proc.as_dict(attrs=['pid', 'name'])
		   # Append dict of process detail in list
		   self.listOfProcessNames.append(pInfoDict)
	def get_pid(self, process_name: str):
		pid = None
		for _pdict in self.listOfProcessNames:
			if _pdict['name'].lower() == process_name.lower():
				pid = _pdict['pid']
				break
		return pid

def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
 
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
 
    return listOfProcObjects
 
def main():
 
    print("*** Iterate over all running process and print process ID & Name ***")
    # Iterate over all running process
    for proc in psutil.process_iter():
        try:
            # Get process name & pid from process object.
            processName = proc.name()
            processID = proc.pid
            print(processName , ' ::: ', processID)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
 
    print('*** Create a list of all running processes ***')
 
    listOfProcessNames = list()
    # Iterate over all running processes
    for proc in psutil.process_iter():
       # Get process detail as dictionary
       pInfoDict = proc.as_dict(attrs=['pid', 'name', 'cpu_percent'])
       # Append dict of process detail in list
       listOfProcessNames.append(pInfoDict)
 
    # Iterate over the list of dictionary and print each elem
    for elem in listOfProcessNames:
        print(elem)
 
    print('*** Top 5 process with highest memory usage ***')
 
    listOfRunningProcess = getListOfProcessSortedByMemory()
 
    for elem in listOfRunningProcess[:5] :
        print(elem)
 
def main2():
    p_o = Processes()
    pidD = p_o.get_pid('Discord.exe')
    pidCC = p_o.get_pid('CrewChiefV4.exe')
    pidSteam = p_o.get_pid('Steam.exe')
    pidRF2 = p_o.get_pid('rFactor2.exe')
    if pidD:
        print(f'Discord {pidD:d}')
    if pidCC:
        print(f'CrewChief {pidCC:d}')
    if pidSteam:
        print(f'Steam {pidSteam:d}')
    if pidRF2:
        print(f'rF2 {pidRF2:d}')

if __name__ == '__main__':
   #main()
   main2()