import evdev
import threading
from evdev import categorize, ecodes


class Device():
    name = 'Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader'

    @classmethod
    def list(cls):
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        for device in devices:
            print("event: " + device.fn, "name: " + device.name, "hardware: " + device.phys)
        return devices

    @classmethod
    def connect(cls):
        device = [dev for dev in cls.list() if cls.name in dev.name][0]
        device = evdev.InputDevice(device.fn)
        return device

    @classmethod
    def run(cls):
        device = cls.connect()
        mylist = []
        try:
            device.grab()
            print("Press Control + c to quit.")
            for event in device.read_loop():
                if len(mylist) == 10:
                    print("".join(i for i in mylist))
                    mylist = []
                if event.type == ecodes.EV_KEY and event.value == 1 and event.code <= 11:
                    c = evdev.ecodes.KEY[event.code].strip("KEY_")
                    mylist.append(c)

        except:
            device.ungrab()
            print('Quitting.')


Device.run()
