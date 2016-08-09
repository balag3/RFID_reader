import evdev
from evdev import categorize, ecodes


class Device():
    name = 'Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader'

    @classmethod
    def list(cls, show_all=False):
        # list the available devices
        devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
        if show_all:
            for device in devices:
                print("event: " + device.fn, "name: " + device.name, "hardware: " + device.phys)
        return devices

    @classmethod
    def connect(cls):
        # connect to device if available
        try:
            device = [dev for dev in cls.list() if cls.name in dev.name][0]
            device = evdev.InputDevice(device.fn)
            return device
        except IndexError:
            print("Device not found.\n - Check if it is properly connected. \n - Check permission of /dev/input/ (see README.md)")
            exit()

    @classmethod
    def run(cls):
        device = cls.connect()
        container = []
        try:
            # bind the device to the script
            device.grab()
            print("RFID scanner is ready....")
            print("Press Control + c to quit.")
            for event in device.read_loop():
                    # enter into an endeless read-loop
                    if event.type == ecodes.EV_KEY and event.value == 1 and event.code <= 11:
                        # filter the input coming from the device and append to our container
                        digit = evdev.ecodes.KEY[event.code].strip("KEY_")
                        container.append(digit)
                    if len(container) == 10:
                        # create and dump the ten digit rfid tag for further use
                        tag = "".join(i for i in container)
                        print(tag)
                        container = []

        except:
            # catch all exceptions to be able release the device
            device.ungrab()
            print('Quitting.')
