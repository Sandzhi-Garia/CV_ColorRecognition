import cv2
import numpy as np

LEDS = {
    'blue': ([90, 80, 80], [130, 255, 255]),
    'yellow': ([15, 80, 80], [40, 255, 255]),
    'green': ([35, 70, 70], [85, 255, 255]),
    'red': ([0, 150, 120], [8, 255, 255])
}

video = cv2.VideoCapture(0)

while True:
    success, img = video.read()
    if not success:
        break
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask_total = np.zeros((480, 640), dtype=np.uint8)
    for color, (lower, upper) in LEDS.items():
        mask = cv2.inRange(hsv, np.array(lower), np.array(upper)).astype(np.uint8)
        mask_total = cv2.bitwise_or(mask_total, mask)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(img, (x, y), (x + w, y + h),  (0, 0, 255), 2)
                cv2.putText(img, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        cv2.imshow("mask", mask_total)
        cv2.imshow("WebCam", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video.release()
cv2.destroyAllWindows()