# Dancing duck
# --------------------
# Importing libraries
from sense_hat import SenseHat
from time import sleep

# Sense HAT
sense = SenseHat()
sense.set_rotation(270, False)

# color sensor
sense.color.gain = 60  
sense.color.integration_cycles = 64  

# colors
rgb = sense.color  # setting color sensor
w = (255, 255, 255)  # white
d = (0, 0, 0)  # black
b = (86, 168, 227)  # blue
y = (255, 242, 0)  # yellow
u = (255, 194, 14)  # dark yellow
x = (rgb.red, rgb.green, rgb.blue) # color sensor

# frames of image
frame01 = [
    b, b, b, y, y, b, b, b,
    b, b, y, y, y, y, b, b,
    b, w, d, y, y, d, w, b,
    b, y, y, u, u, y, y, b,
    b, b, y, y, y, y, b, b,
    b, y, y, y, y, y, y, b,
    b, y, y, y, y, y, y, b,
    b, b, y, y, y, y, b, b
]

frame02 = [
    b, b, y, y, b, b, b, b,
    b, y, y, y, y, b, b, b,
    w, d, y, y, d, w, b, b,
    y, y, u, u, y, y, b, b,
    b, y, y, y, y, b, b, b,
    y, y, y, y, y, y, b, b,
    y, y, y, y, y, y, b, b,
    b, y, y, y, y, b, b, b
]

frame03 = [
    b, b, b, b, y, y, b, b,
    b, b, b, y, y, y, y, b,
    b, b, w, d, y, y, d, w,
    b, b, y, y, u, u, y, y,
    b, b, b, y, y, y, y, b,
    b, b, y, y, y, y, y, y,
    b, b, y, y, y, y, y, y,
    b, b, b, y, y, y, y, b
]

# First loop - background is blue 
for i in range(7):
    sense.set_pixels(frame01)
    sleep(0.5)
    sense.set_pixels(frame02)
    sleep(0.5)
    sense.set_pixels(frame01)
    sleep(0.5)
    sense.set_pixels(frame03)
    sleep(0.5)
    sense.set_pixels(frame01)

# Second loop - background is what color sensor see
for i in range(7):
    frame01_rgb = [x if pixel == b else pixel for pixel in frame01]
    frame02_rgb = [x if pixel == b else pixel for pixel in frame02]
    frame03_rgb = [x if pixel == b else pixel for pixel in frame03]
    
    sense.set_pixels(frame01_rgb)
    sleep(0.5)
    sense.set_pixels(frame02_rgb)
    sleep(0.5)
    sense.set_pixels(frame01_rgb)
    sleep(0.5)
    sense.set_pixels(frame03_rgb)
    sleep(0.5)
    sense.set_pixels(frame01_rgb)
