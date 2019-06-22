class StatusDisplay:
    def __init__(self, _processNames): # processNames are not used in this simple print implementation
        pass
    def processNotFound(self, processName):
        print(f"Warning: process '{processName}' not running")
    def buttonNotFound(self, buttonName):
        print(f"Error: button '{buttonName}' not found")
    def currentProcess(self, processName):
        print(f"Current process '{processName}'")
    def displayVolume(self, volume):
        print(f"Volume: {volume}")
