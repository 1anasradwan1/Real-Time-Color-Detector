import cv2
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)

if not capture.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = capture.read()
    if not ret:
        print("Failed to grab frame")
        break

    height, width, _ = frame.shape
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cx = int(width / 2)
    cy = int(height / 2)
    pixel_value = hsv_frame[cy, cx]
    huv_Value = pixel_value[0] 
    sat = pixel_value[1]        
    val = pixel_value[2]        

    
    if sat < 40 and val > 200:
        color = "White"
    elif val < 50:
        color = "Black"
    elif sat < 40:
        color = "Gray"
    elif 0 <= huv_Value < 8 or 172 <= huv_Value <= 180:
        color = "Red"
    elif 8 <= huv_Value < 18:
        color = "Orange"
    elif 18 <= huv_Value < 26:
        color = "Yellow"
    elif 35 <= huv_Value < 85:
        color = "Green"
    elif 85 <= huv_Value < 100:
        color = "Cyan"
    elif 100 <= huv_Value < 130:
        color = "Blue"
    elif 130 <= huv_Value < 145:
        color = "Violet"
    else:
        color = "Unknown"

    print("Color:", color, "HSV:", pixel_value)

    cv2.putText(frame, color, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 4)
    cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)  
    cv2.imshow("frame", frame)


    key = cv2.waitKey(1)
    if key == 27:  # Press 'ESC' to exit
        break

capture.release()
cv2.destroyAllWindows()