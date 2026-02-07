def right():
    pins.servo_write_pin(AnalogPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 90)
def left():
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 180)
def stop():
    pins.servo_write_pin(AnalogPin.P1, 90)
    pins.servo_write_pin(AnalogPin.P2, 90)

def on_button_pressed_a():
    forward()
input.on_button_pressed(Button.A, on_button_pressed_a)

def backward():
    pins.servo_write_pin(AnalogPin.P1, 180)
    pins.servo_write_pin(AnalogPin.P2, 0)

def on_button_pressed_ab():
    left()
    basic.pause(500)
    right()
    basic.pause(500)
    backward()
    basic.pause(500)
    forward()
    basic.pause(500)
    stop()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    stop()
input.on_button_pressed(Button.B, on_button_pressed_b)

def setup():
    global strip
    strip = neopixel.create(DigitalPin.P0, 5, NeoPixelMode.RGB)
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
def forward():
    pins.servo_write_pin(AnalogPin.P1, 0)
    pins.servo_write_pin(AnalogPin.P2, 180)
strip: neopixel.Strip = None
setup()