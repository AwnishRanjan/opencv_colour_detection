import cv2
from utils import get_limits
from PIL import Image
# read 


webcam = cv2.VideoCapture(0)  # camera to initial 


colour = []

# Take input for each RGB component

r = int(input('Enter the red component to detect (0-255): '))
g = int(input('Enter the green component to detect (0-255): '))
b = int(input('Enter the blue component to detect (0-255): '))

# Add the RGB values to the color list
colour = [r, g, b]

print('RGB code entered:', colour)



# visualise 
while True:
    ret,frame = webcam.read()

    hsv_img = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_limit , upper_limit = get_limits(color=colour)

    mask = cv2.inRange(hsv_img,lower_limit,upper_limit)
     
    mask_= Image.fromarray(mask)

    bbox = mask_.getbbox()

    if bbox is not None:
        X1,y1,X2,y2 = bbox 
        color = (0, 255, 0)  # RGB color (here, it's green)
        thickness = 2  # Thickness of the rectangle border
        print(bbox)
        text = 'press q to stop '
        frame = cv2.putText(frame, text, (50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,255),2)

        frame = cv2.rectangle(frame,(X1,y1),(X2,y2),color,thickness)
   
    cv2.imshow('frame',frame)
    if cv2.waitKey(50)  & 0XFF  == ord('q'):
        break 


webcam.release()
cv2.destroyAllWindows()
