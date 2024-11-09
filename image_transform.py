import cv2
import os

# prompt user for the image path
image_path = input("Enter the path to the image. \n(eg. C:/Users/user/year4/ee347/labpractice/garnacho.jpg): \n")

#convert Windows path to WSL path if needed
if ":" in image_path:
    # convert `C:/path` or `C:\path` format to `/mnt/c/path`
    drive_letter = image_path[0].lower()  # get drive letter and convert to lowercase
    image_path = f"/mnt/{drive_letter}" + image_path[2:].replace("\\", "/").replace(":", "")

# load the image from the specified path
image = cv2.imread(image_path)

#check if the image was successfully loaded
if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit(1)

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", grayscale_image)
cv2.imwrite("grayscale.jpg", grayscale_image)

blurred_image = cv2.GaussianBlur(grayscale_image, (5, 5), 0)
cv2.imshow("Blurred Image", blurred_image)
cv2.imwrite("blurred.jpg", blurred_image)

edges_image = cv2.Canny(blurred_image, 50, 150)
cv2.imshow("Edge Detection", edges_image)
cv2.imwrite("edges.jpg", edges_image)


cv2.waitKey(0)
cv2.destroyAllWindows()
