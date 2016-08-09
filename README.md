# RFID_reader

### Designed to use with the 'Sycreader RFID Technology Co., Ltd SYC ID&IC USB Reader'
### With minor changes can be used with any RFID reader device.
### The program binds the rfid reader to the terminal which started the script.
### This way the terminal only accepts input from the device and can be run in the background.
### You can stop the script with the Control + c key combination.
### Before running the script you have to set permission of /dev/input/
### by ```sudo chown <user who runs the script> -R /dev/input/```  

## Known issues
### After reconnecting the device or force stopping the script (Control + z) permission have to be set again.Otherwise the device won't be seen.

## External libraries
### - evdev python library
```pip3 install evdev```
