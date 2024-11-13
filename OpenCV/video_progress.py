import cv2
import os

# load the video
video_path = '/mnt/c/Users/user/year4/ee347/labpractice/input_video.mp4'

# TROUBLESHOOTING
if not os.path.exists(video_path):
    print("Error: Video file not found at specified path.")
    exit()

output_path = 'output_video.mp4'
cap = cv2.VideoCapture(video_path)

# TROUBLESHOOTING
if not cap.isOpened():
    print("Error: Could not open input video.")
    exit()

# get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height), isColor=False)

# TROUBLESHOOTING
if not out.isOpened():
    print("Error: Could not open VideoWriter.")
    exit()

# process each frame
current_frame = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate the progress
    progress = current_frame / total_frames

    # draw the progress bar at the bottom of the frame
    bar_width = int(frame_width * progress)
    bar_height = 20
    bar_colour = (255)

    # filled rectangle for progress bar
    gray_frame[-bar_height:, :bar_width] = bar_colour

    # write modified frame to output video
    out.write(gray_frame)
    #update current frame count
    current_frame += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print("Video processing complete. Saved as 'output_video.mp4'.")