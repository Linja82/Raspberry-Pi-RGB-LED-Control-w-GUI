# Raspberry-Pi-RGB-LED-Control-w-GUI
A Python script that allows you to control a common anode RGB LED from a GUI on the Raspberry Pi

## Wiring
In the current configuration of the code the pins are connected as such:  
Red:	Pin 11  
Green:	Pin 15  
Blue:	Pin 13  
  
Note: The pin numbers follow BOARD numbering, not BCM.

## Resistors:  
Red:	200 Ω  
Green:	100 Ω  
Blue:	100 Ω

## GUI
![alt text](https://github.com/Linja82/Raspberry-Pi-RGB-LED-Control-w-GUI/blob/main/Images/GUI_Screenshot.png "GUI Screenshot")
  
Use the sliders to select the RGB value you want displayed on the LED.  
  
When closing the app, it is recommended that you use the "Exit" button. The "Exit" button includes a GPIO cleanup command. Exiting without this may cause GPIO issues.