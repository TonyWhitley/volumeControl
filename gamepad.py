# pylint: skip-file
# type: ignore
"""Simple example showing how to get gamepad events."""
#https://github.com/zeth/inputs

from __future__ import print_function


from inputs import get_gamepad


def main():
    """Just print out some event infomation when the gamepad is used."""

    from inputs import devices
    for device in devices:
      print(device)
    while 1:
        events = get_gamepad()
        for event in events:
            print(event.ev_type, event.code, event.state)


if __name__ == "__main__":
    main()

