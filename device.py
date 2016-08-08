import evdev
import threading
from evdev import categorize, ecodes


class Device():
    name = 'Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader'

    @classmethod
    def list(cls,show_all=False):
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        if show_all:
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
        container = []
        try:
            device.grab()
            print("RFID scanner is ready....")
            print("Press Control + c to quit.")
            for event in device.read_loop():
                if len(container) == 10:
                    tag = "".join(i for i in container)
                    print(tag)
                    container = []
                if event.type == ecodes.EV_KEY and event.value == 1 and event.code <= 11:
                    digit = evdev.ecodes.KEY[event.code].strip("KEY_")
                    container.append(digit)

        except:
            device.ungrab()
            print('Quitting.')


Device.run()
