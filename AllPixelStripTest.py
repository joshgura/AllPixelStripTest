from bibliopixel.animation import BaseStripAnim
from bibliopixel.animation import BaseAnimation

class StripChannelTest(BaseStripAnim):

    def __init__(self, led):
        super(StripChannelTest, self).__init__(led)
        self._internalDelay = 500
        self.colors = [colors.Red, colors.Green, colors.Blue, colors.White]

    def step(self, amt=1):

        self._led.set(0, colors.Red)
        self._led.set(1, colors.Green)
        self._led.set(2, colors.Green)
        self._led.set(3, colors.Blue)
        self._led.set(4, colors.Blue)
        self._led.set(5, colors.Blue)

        color = self._step % 4
        self._led.fill(self.colors[color], 7, 9)

        self._step += 1
		
import bibliopixel
#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

#Load driver for the AllPixel
from bibliopixel.drivers.serial_driver import *
#set number of pixels & LED type here 
driver = DriverSerial(num = 20, type = LEDTYPE.LPD8806)

#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)

#load channel test animation
#from bibliopixel.animation import StripChannelTest
anim = StripChannelTest(led)

try:
	#run the animation
    anim.run()
except KeyboardInterrupt:
	#Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()