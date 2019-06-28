# pylint: skip-file
# type: ignore
"""
Mutes the volume of all processes, but unmutes Firefox process.

https://github.com/AndreMiras/pycaw
"""
from pycaw.pycaw import AudioUtilities

class Audio:
    def __init__(self):
        self.sessions = AudioUtilities.GetAllSessions()
    def set_volume(self, process_name: str, volume: float):
        for session in self.sessions:
            if session.Process:
                #print(session.Process.name(), session.Process.pid)
                if session.Process.name() == process_name:
                    volume_o = session.SimpleAudioVolume
                    volume_o.SetMasterVolume(volume, None)


def x():
        mgr = AudioUtilities.GetAudioSessionManager()
        if mgr is None:
            return audio_sessions
        sessionEnumerator = mgr.GetSessionEnumerator()
        count = sessionEnumerator.GetCount()
        print(count)
        for i in range(count):
            pass

def main():
    x()
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if session.Process:
            print(session.Process.name(), session.Process.pid)
        if session.Process and session.Process.name() == "rFactor2.exe":
            volume.SetMasterVolume(0.9, None)
        else:
            pass
            #volume.SetMute(0, None)


if __name__ == "__main__":
    main()
    pass


