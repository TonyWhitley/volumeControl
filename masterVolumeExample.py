"""
Get and set access to master volume example.

https://github.com/AndreMiras/pycaw
https://stackoverflow.com/questions/20938934/controlling-applications-volume-by-process-id/20982715#20982715
https://docs.microsoft.com/en-gb/windows/desktop/CoreAudio/getting-the-default-device-endpoint-for-stream-routing

"""
from __future__ import print_function

from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def main():
    devices = AudioUtilities.GetSpeakers()
    allDevices = AudioUtilities.GetAllDevices()
    for dev in allDevices:
        if dev.FriendlyName == 'Headphones (Rift Audio)':
            pass
    sessions = AudioUtilities.GetAllSessions()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    print("volume.GetMute(): %s" % volume.GetMute())
    print("volume.GetMasterVolumeLevel(): %s" % volume.GetMasterVolumeLevel())
    print("volume.GetVolumeRange(): (%s, %s, %s)" % volume.GetVolumeRange())
    print("volume.SetMasterVolumeLevel()")
    volume.SetMasterVolumeLevel(volume.GetMasterVolumeLevel()/1.5, None)
    print("volume.GetMasterVolumeLevel(): %s" % volume.GetMasterVolumeLevel())


if __name__ == "__main__":
    main()
