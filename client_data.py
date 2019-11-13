
# Python program to implement  
# WebCam Motion Detector 
  
# importing OpenCV, time and Pandas library 
import cv2, time
#, # pandas 
# importing datetime class from datetime library 
from datetime import datetime 
  
  
 


# Assigning our static_back to None 
static_back = None
  
# List when any moving object appear 
motion_list = [ None, None ] 
  
# Time of movement 
time = [] 
frames_tracked = False

# Capturing video 
video = cv2.VideoCapture(0) 
filename = 0
# Infinite while loop to treat stack of image as video 
while True: 
    # Reading frame(image) from video 
    check, frame = video.read() 
  
    # Initializing motion = 0(no motion) 
    motion = 0
  
    # Converting color image to gray_scale image 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
  
    # Converting gray scale image to GaussianBlur  
    # so that change can be find easily 
    gray = cv2.GaussianBlur(gray, (21, 21), 0) 
  
    # In first iteration we assign the value  
    # of static_back to our first frame 
    if static_back is None: 
        static_back = gray 
        continue
  
    # Difference between static background  
    # and current frame(which is GaussianBlur) 
    diff_frame = cv2.absdiff(static_back, gray) 
    
    # If change in between static background and 
    # current frame is greater than 30 it will show white color(255) 
    thresh_frame = cv2.threshold(diff_frame, 40, 255, cv2.THRESH_BINARY)[1] 
    thresh_frame = cv2.dilate(thresh_frame, None, iterations = 2) 
  
    # Finding contour of moving object 
    (cnts, _) = cv2.findContours(thresh_frame.copy(),  
                       cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
  
    for contour in cnts: 
        if cv2.contourArea(contour) < 10000: 
            continue
        motion = 1
  
  
    # Appending status of motion 
    motion_list.append(motion) 
  
    motion_list = motion_list[-2:] 
    
    # Appending Start time of motion 
    if motion_list[-1] == 1 and motion_list[-2] == 0:
        print("test")
        frames_tracked = True
        
        time.append(datetime.now()) 
        
    
    if frames_tracked == True:
        count += 1
    else:
        count = 0
    if count == 7:
        filename +=1
        cv2.imwrite(str(filename) + 'test.png', frame)

    # Appending End time of motion 
    if motion_list[-1] == 0 and motion_list[-2] == 1: 
        print("done")
        frames_tracked = False
        time.append(datetime.now()) 
        
        

    key = cv2.waitKey(1) 
    # if q entered whole process will stop 
    if key == ord('q'): 
        # if something is movingthen it append the end time of movement 
        if motion == 1: 
            time.append(datetime.now()) 
        break
  
  
video.release() 
  
# Destroying all the windows 
cv2.destroyAllWindows() 


