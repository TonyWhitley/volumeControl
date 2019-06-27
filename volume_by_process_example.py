# pylint: skip-file
# type: ignore
"""
Mutes the volume of all processes, but unmutes Firefox process.

https://github.com/AndreMiras/pycaw
"""
from pycaw.pycaw import AudioUtilities

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


