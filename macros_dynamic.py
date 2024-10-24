# DO NOT USE IF YOU HAVE YOUR OWN MACRO DEVICE OR DON'T COMMIT :)
import os
import sys
import evdev

if not os.geteuid() == 0:
    sys.exit("Run this command as root")

scriptpath = os.getcwd() + '/'

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]

dev = None
# Name of device to look for
deviceToLookFor = 'SEMICO USB Keyboard'

for device in devices:
    # Check if device is the one that I want and sets that to the input device
    if deviceToLookFor in device.name and 'input0' in device.phys:
        dev = evdev.InputDevice(device.path)
        break

# DISABLE ALL DEVICES THAT CORRESPOND WITH THE ONE I PUT AS MY MACRO DEVICE
xinput_devices = os.popen("xinput list | grep 'SEMICO' | grep 'keyboard' | cut -d '=' -f 2 | cut -f 1").read()
xinput_devices_array = xinput_devices.split('\n')
for xinput_device in xinput_devices_array:
    os.system('/usr/bin/xinput --disable ' + xinput_device)
    print('disabled device with id:', xinput_device)

if dev is None:
    sys.exit("No device was found")

for event in dev.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        key = evdev.categorize(event)
        if key.keystate == key.key_down:
            if key.keycode == 'KEY_Q':
                os.system('/bin/bash '+ scriptpath + 'warden_start_list.sh')
            if key.keycode == 'KEY_W':
                os.system('/bin/bash '+ scriptpath + 'warden_dev_update.sh')
            if key.keycode == 'KEY_T':
                os.system('/bin/bash '+ scriptpath + 'warden_stop.sh')
            if key.keycode == 'KEY_A':
                os.system('/bin/bash '+ scriptpath + 'warden_services.sh')
            if key.keycode == 'KEY_C':
                os.system('/usr/bin/xdotool key XF86AudioPrev')
            if key.keycode == 'KEY_V':
                os.system('/usr/bin/xdotool key XF86AudioPlay')
            if key.keycode == 'KEY_B':
                os.system('/usr/bin/xdotool key XF86AudioNext')

