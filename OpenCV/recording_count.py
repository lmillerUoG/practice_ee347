import cv2
import datetime

# initialise video capture from the default camera
cap = cv2.VideoCapture(0)

recording = False       # indicates whether recording is in progress
out = None              # placeholder for the video writer object
recording_count = 1     # counter to create unique file names

# capture and display video frames:
while True:
    ret, frame = cap.read()     # read frame from camera
    if not ret:
        break

    # add red dot if recording
    if recording:
        cv2.circle(frame, (frame.shape[1] - 20, 20), 10, (0, 0, 255), -1)

    cv2.imshow("Video", frame)

    # key bindings for recording and exiting
    key = cv2.waitKey(1) & 0xFF

    # press 'r' to toggle recording
    if key == ord('r'):
        if not recording:
            # start recording
            filename = f"recorded_video_{recording_count}.mp4"
            out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'mp4v'), 20, (frame.shape[1], frame.shape[0]))
            print(f"Recording started: {filename}")
            recording = True
            recording_count += 1        #increment count for the next video file
        else:
            # stop recording
            print(f"Recording stopped.")
            recording = False
            out.release()               # release video writer

    # press 'q' to quit
    elif key == ord('q'):
        if recording:
            out.release()   # ensure writer is released if recording
        print("Exiting...")
        break

    # write frame to video if recording
    if recording and out is not None:
        out.write(frame)

cap.release()
if out is not None:
    out.release()
cv2.destroyAllWindows()
