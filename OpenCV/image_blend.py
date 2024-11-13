import cv2
import numpy as np

#load background and logo images
background = cv2.imread("/mnt/c/Users/user/year4/ee347/labpractice/background.jpg")
logo = cv2.imread("/mnt/c/Users/user/year4/ee347/labpractice/logo.png", cv2.IMREAD_UNCHANGED)

# check if images laoded successfully
if background is None:
    print("Error: Could not load background.jpg")
    exit(1)

if logo is None:
    print("Error: Could not load logo.png")
    exit(1)

# resize the logo to 20% of the background's height (maintains aspect ratio)
logo_height = int(background.shape[0] * 0.2)
logo_aspect_ratio = (logo.shape[1]/ logo.shape[0])
logo_width = int((logo_aspect_ratio) * logo_height) #maintain aspect ratio

resized_logo = cv2.resize(logo, (logo_width, logo_height))

# create a mask for the logo
#check if logo has an alpha channel (transparency)
if resized_logo.shape[2] == 4:
    alpha_channel = resized_logo[:, :, 3]
    _, mask = cv2.threshold(alpha_channel, 1, 255, cv2.THRESH_BINARY)
    logo_rgb = resized_logo[:, :, :3]   #remove alpha channel from logo for blending
else:
    #if no alpha channel, create a binary mask from the logo's brightness
    logo_rgb = resized_logo
    gray_logo = cv2.cvtColor(logo_rgb, cv2.COLOR_BGR2GRAY)
    _, mask = cv2.threshold(gray_logo, 1, 255, cv2.THRESH_BINARY)

# position the logo at the bottom-right of the background
y_offset = background.shape[0] - logo_rgb.shape[0]
x_offset = background.shape[1] - logo_rgb.shape[1]

# define region of interest on the background
roi = background[y_offset:y_offset+logo_rgb.shape[0], x_offset:x_offset+logo_rgb.shape[1]]

# use the mask to blend the logo with the roi on the background
background_part = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask))
logo_part = cv2.bitwise_and(logo_rgb, logo_rgb, mask=mask)
blended_part = cv2.addWeighted(background_part, 1, logo_part, 0.7, 0)

#place the blended part back into the background
background[y_offset:y_offset+logo_rgb.shape[0], x_offset:x_offset+logo_rgb.shape[1]] = blended_part

cv2.imshow("Blended Image", background)
cv2.imwrite("blended_output.jpg", background)
cv2.waitKey(0)
cv2.destroyAllWindows()