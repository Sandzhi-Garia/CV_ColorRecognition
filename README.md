This is my first OpenCV project that detects objects, recognizes their colors in real time and lights the LEDs of the corresponding color. 
Multiple objects can be detected simultaneously using WebCam. 

Tech Stack: VS Code (Python + OpenCV) and Arduino IDE (C/C++). I used Arduino Nano to turn on/off the LEDs using Serial command.

The folder contains two .py files: 
- 'main.py' was my first version of the project and just detects colors with no LEDs.

- 'Arduino_main.py' is the full version, sends LED states to Arduino via Serial.

- 'Nano_LEDS_for_CV.ino' is an Arduino sketch that reads Serial and controls LEDs.

How to run:
1. Upload 'Nano_LEDS_for_CV.ino' to Arduino Nano
2. Connect LEDs to pins 9 (Red), 10 (Green), 11 (Blue), 6 (Yellow)
3. Update `COM` port in `Arduino_main.py`
4. Run the file
