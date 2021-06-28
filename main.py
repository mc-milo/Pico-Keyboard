import time # to stop bugs  ## note use asyncio when it comes to the pico lib ##
import board # for the gpio pins
import digitalio # to say if the button has power or no
import usb_hid # to use it as a keyboard
from adafruit_hid.keyboard import Keyboard # to press keys
from adafruit_hid.keycode import Keycode # to say which keys to press


'''
define which button is which gpio pin
'''

btn1_pin = board.GP15
btn2_pin = board.GP14
btn3_pin = board.GP13
btn4_pin = board.GP12


keyboard = Keyboard(usb_hid.devices) # define the usb device as a keyboard


''' 
define the buttons pull direction and the pins 
'''

btn1 = digitalio.DigitalInOut(btn1_pin)
btn1.direction = digitalio.Direction.INPUT
btn1.pull = digitalio.Pull.DOWN

btn2 = digitalio.DigitalInOut(btn2_pin)
btn2.direction = digitalio.Direction.INPUT
btn2.pull = digitalio.Pull.DOWN

btn3 = digitalio.DigitalInOut(btn3_pin)
btn3.direction = digitalio.Direction.INPUT
btn3.pull = digitalio.Pull.DOWN

btn4 = digitalio.DigitalInOut(btn4_pin)
btn4.direction = digitalio.Direction.INPUT
btn4.pull = digitalio.Pull.DOWN


while True: # infinite loop to work all the time
    ## press alt tab ##
    if btn1.value: # when power is passed it will be True when its not its False
        print("1") # chech not mandatory
        keyboard.press(Keycode.ALT, Keycode.TAB) # press alt tab
        time.sleep(0.1) # !!!if this not here its will bug!!!
        keyboard.release(Keycode.ALT, Keycode.TAB) # release alt tab 

    ## open vs code ##
    elif btn2.value: # when power is passed it will be True when its not its False
        print("2") # chech not mandatory
        keyboard.press(Keycode.GUI, Keycode.R) # press windows r
        keyboard.release(Keycode.GUI, Keycode.R) # release windows ar
        time.sleep(0.1) # !!!if this not here its will bug!!!
        keyboard.press(Keycode.C) # press c
        keyboard.release(Keycode.C) # release c
        time.sleep(0.1) # !!!if this not here its will bug!!!
        keyboard.press(Keycode.O) # press o
        keyboard.release(Keycode.O) # release o
        time.sleep(0.1) # !!!if this not here its will bug!!!
        keyboard.press(Keycode.D) # press d
        keyboard.release(Keycode.D) # release d
        time.sleep(0.1) # !!!if this not here its will bug!!!
        keyboard.press(Keycode.E) # press e
        keyboard.release(Keycode.E) # release e
        time.sleep(0.1)
        keyboard.press(Keycode.ENTER) # press enter
        time.sleep(0.1) # !!!if this not here its will bug!!!
        keyboard.release(Keycode.ENTER) # release enter
        
    ## screenshot on win 10 ##
    elif btn3.value: # when power is passed it will be True when its not its False
        print("3") # chech not mandatory
        keyboard.press(Keycode.GUI, Keycode.SHIFT, Keycode.S) # press win shift s
        time.sleep(0.1) # !!!if this not here its will bug!!!
        keyboard.release(Keycode.GUI, Keycode.SHIFT, Keycode.S) # release win shift s

    ## clip save of 5 min on radeon software ##
    elif btn4.value: # when power is passed it will be True when its not its False
        print("4") # chech not mandatory
        keyboard.press(Keycode.CONTROL, Keycode.SHIFT, Keycode.BACKSLASH) # press ctrl shift \
        time.sleep(0.1) # !!!if this not here its will bug!!!
        keyboard.release(Keycode.CONTROL, Keycode.SHIFT, Keycode.BACKSLASH) # release ctrl shift \

    time.sleep(0.1) # !!!if this not here its will bug!!!