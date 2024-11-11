import cv2


# define input and output paths
video_path = '/mnt/c/Users/user/year4/ee347/labpractice/input_video.mp4'
output_path = 'timestamped_video.mp4'

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open input video.")
    exit()

# get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

if not out.isOpened():
    print("Erroe: Could not open VideoWriter.")
    exit()

current_frame = 0
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # calculate timestamp in seconds
    timestamp_seconds = current_frame / fps

    # fromat timestamp as HH:MM:SS
    hours = int(timestamp_seconds // 3600)
    minutes = int((timestamp_seconds % 3600) // 60)
    seconds = int(timestamp_seconds % 60)
    timestamp = f"{hours:02}:{minutes:02}:{seconds:02}"

    # overlay the timestamp text on the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    font_colour = (255, 255, 255) #white
    thickness = 2
    position = (10, 30) #top-left corner

    cv2.putText(frame, timestamp, position, font, font_scale, font_colour, thickness, cv2.LINE_AA)

    # write modified frame to output video
    out.write(frame)

    # move to next frame
    current_frame += 1

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video processing complete. Saved as '{output_path}.")