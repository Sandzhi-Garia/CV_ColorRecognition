import cv2
import numpy as np
import serial

LEDS = {
    'blue': ([90, 80, 80], [130, 255, 255]),
    'yellow': ([15, 80, 80], [40, 255, 255]),
    'green': ([35, 70, 70], [85, 255, 255]),
}

video = cv2.VideoCapture(0)
ser = serial.Serial('COM3', 9600) 
while True:
    success, img = video.read()
    if not success:
        break
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask_total = np.zeros((480, 640), dtype=np.uint8)
    best_color = None
    
    for color, (lower, upper) in LEDS.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper)).astype(np.uint8)
        mask_total = cv2.bitwise_or(mask_total, mask)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            if cv2.contourArea(contour) > 500:
                best_color = color
                best_contour = contour

    mask_red1 = cv2.inRange(hsv, np.array([0, 150, 120]), np.array([8, 255, 255])).astype(np.uint8)
    mask_red2 = cv2.inRange(hsv, np.array([170, 150, 120]), np.array([180, 255, 255])).astype(np.uint8)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    mask_total = cv2.bitwise_or(mask_total, mask_red)

    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_red:
        if cv2.contourArea(contour) > 500:
            best_color = 'red'
            best_contour = contour

    if best_color:
        x, y, w, h = cv2.boundingRect(best_contour)
        cv2.rectangle(img, (x, y), (x + w, y + h),  (0, 0, 255), 2)    
        cv2.putText(img, best_color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        commands = {
            'blue': 'B',
            'yellow': 'Y',
            'green': 'G',
            'red': 'R'
        }
        ser.write(commands[best_color].encode())
        
    cv2.imshow("mask", mask_total)
    cv2.imshow("WebCam", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()