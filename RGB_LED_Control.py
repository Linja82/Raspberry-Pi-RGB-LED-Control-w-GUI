from tkinter import *
import RPi.GPIO as GPIO
import time

##### NOTES #####
# The common anode pin connects to the 3.3V rail
# Duty cycle values need to be inverted because the LED is common anode
# Higher duty cycle reduces the voltage difference between the GPIO pin and the 3.3V rail

colour_pins = [11, 15, 13] # Red, Green, Blue


def setup():    # Initiates the GPIO pins and pwm
    global pwmR, pwmG, pwmB
    GPIO.setmode(GPIO.BOARD)
    
    for i in colour_pins:         # Sets pin mode and state for all 3 LED pins
        GPIO.setup(i, GPIO.OUT)
        GPIO.output(i, GPIO.LOW)

    pwmR = GPIO.PWM(colour_pins[0], 8000)
    pwmG = GPIO.PWM(colour_pins[1], 8000)
    pwmB = GPIO.PWM(colour_pins[2], 8000)

    pwmR.start(0)
    pwmG.start(0)
    pwmB.start(0)


def setColour(r_in, g_in, b_in): # 0 ~ 255 values
    r = round(((255 - r_in) / 255) * 100)
    g = round(((255 - g_in) / 255) * 100)
    b = round(((255 - b_in) / 255) * 100)

    pwmR.ChangeDutyCycle(r)
    print("Red " + str(r) + " / " + str(r_in))

    pwmG.ChangeDutyCycle(g)
    print("Green " + str(g) + " / " + str(g_in))

    pwmB.ChangeDutyCycle(b)
    print("Blue " + str(b) + " / " + str(b_in))

    print("\n")


def shutdown():
    pwmR.stop()
    pwmG.stop()
    pwmB.stop()
    GPIO.cleanup()
    window.destroy()
    exit()


# Program start

setup()

window = Tk()
window.title("RGB LED Control")
window.geometry("280x360")

# Create the widgets
red_label = Label(window, text="Red")
red_slider = Scale(window, from_=255, to=0, length=300, resolution=1, orient=VERTICAL)

green_label = Label(window, text="Green")
green_slider = Scale(window, from_=255, to=0, length=300, resolution=1, orient=VERTICAL)

blue_label = Label(window, text="Blue")
blue_slider = Scale(window, from_=255, to=0, length=300, resolution=1, orient=VERTICAL)

# Place the widgets on a grid
red_label.grid(row=0, column=0, padx=(60, 0))
red_slider.grid(row=1, column=0, padx=(30, 0))

green_label.grid(row=0, column=1, padx=(25, 0))
green_slider.grid(row=1, column=1)

blue_label.grid(row=0, column=2, padx=(26, 0))
blue_slider.grid(row=1, column=2)


leave = Button(window, text="Exit", command = shutdown).grid(row=2, column=1, padx=(30, 0))

LOOP_ACTIVE = True
while LOOP_ACTIVE:
    window.update()

    # Display colour here
    setColour(red_slider.get(), green_slider.get(), blue_slider.get())
    time.sleep(0.5)