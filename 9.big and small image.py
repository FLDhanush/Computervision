from PIL import Image 
Original_Image = Image.open(r"C:\Users\keert\Downloads\wallpaperflare.com_wallpaper (1).jpg") 
rotated_image1 = Original_Image.rotate(180) 
rotated_image2 = Original_Image.transpose(Image.ROTATE_90) 
rotated_image3 = Original_Image.rotate(60)
rotated_image4 = Original_Image.rotate(270)
rotated_image0 = Original_Image.rotate(90) 
rotated_image1.show() 
rotated_image2.show() 
rotated_image3.show()
rotated_image4.show() 
rotated_image0.show()
