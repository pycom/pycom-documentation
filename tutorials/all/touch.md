# Touch

Example of how to use the Touch class of the Machine module:

```python
from machine import Touch
from machine import Timer
import time


class TouchPad:

    def __init__(self, pin, name):
        self.touch = Touch(pin)
        self.last_press = 0
        self.name = name
        self.pressed = False

    def ispressed(self):
        if self.touch.read() < (self.touch.init_value() * 2 / 3):
            self.pressed = True
        else:
            self.pressed = False
        return self.pressed

    def just_pressed(self):
        now = time.ticks_ms()
        if now - self.last_press < 500:
            return True
        else:
            return False

    def set_press(self):
        self.last_press = time.ticks_ms()


class TouchController:

    def __init__(self, pads):
        self.pads = pads
        for pad in self.pads:
            pad.touch.init_value(1500)

    def check(self, alarm):
        for pad in self.pads:
            if pad.ispressed() and not pad.just_pressed():
                pad.set_press()
                if pad.name == 'Right':
                    if tleft.just_pressed():
                        print('Swipe right')
                    else:
                        print('{} pressed'.format(pad.name))
                elif pad.name == 'Left':
                    if tright.just_pressed():
                        print('Swipe left')
                    else:
                        print('{} pressed'.format(pad.name))
                elif pad.name == 'Up':
                    if tbott.just_pressed():
                        print('Swipe up')
                    else:
                        print('{} pressed'.format(pad.name))
                elif pad.name == 'Bottom':
                    if tupp.just_pressed():
                        print('Swipe down')
                    else:
                        print('{} pressed'.format(pad.name))


tleft = TouchPad('P4', 'Left')
tright = TouchPad('P8', 'Right')
tbott = TouchPad('P9', 'Bottom')
tupp = TouchPad('P23', 'Up')

# initialize the touch controller
touch_controller = TouchController(pads=[tleft, tright, tbott, tupp])

# enable the alarm to check the status
Timer.Alarm(touch_controller.check, ms=10, periodic=True)
```