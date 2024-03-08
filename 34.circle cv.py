import cv2  
    
# path  
path = r'C:\Users\Rajnish\Desktop\geeksforgeeks\geeks.png'
    
# Reading an image in default mode 
image = cv2.imread(path) 
    
# Window name in which image is displayed 
window_name = 'Image'
   
# Center coordinates 
center_coordinates = (120, 50) 
  
# Radius of circle 
radius = 20
   
# Blue color in BGR 
color = (255, 0, 0) 
   
# Line thickness of 2 px 
thickness = 2
   
# Using cv2.circle() method 
# Draw a circle with blue line borders of thickness of 2 px 
image = cv2.circle(image, center_coordinates, radius, color, thickness) 
   
# Displaying the image  
cv2.imshow(window_name, image)
