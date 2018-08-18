__author__ = 'bendik'
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()
pressure = sense.get_pressure()
sense.show_message("lufttrykk: " +str(pressure) + " millibar")

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

while True:
    temp = sense.temp
    temp_value = temp / 2.5 + 16
    pixels = [red if i < temp_value else white for i in range(64)]
    sense.set_pixels(pixels)