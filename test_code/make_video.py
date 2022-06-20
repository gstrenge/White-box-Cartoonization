import cv2
import sys
import os



filename = sys.argv[1]
skip = int(sys.argv[2])
framerate = float(sys.argv[3])


test_img = cv2.imread(os.path.abspath(f"{filename}-1.png"))
height, width, _ = test_img.shape

writer = cv2.VideoWriter(filename=f"{filename}_skip{skip}_fps{framerate}.avi",  #Provide a file to write the video to
fourcc=cv2.VideoWriter_fourcc('M','J', 'P', 'G'),            #Use whichever codec works for you...
fps=framerate,                                        #How many frames do you want to display per second in your video?
frameSize=(width, height))   

index = 1
frame = None

while True:

    frame = cv2.imread(os.path.abspath(f"{filename}-{index}.png"))
    if frame is None:
        if index == 5534:
            break
        index += skip
        continue
    cv2.imshow(f"Frame", frame)
    key_pressed = cv2.waitKey(10)
    if key_pressed == 27:                           #Escape key
        break
    writer.write(frame)
    index += skip

writer.release()
cv2.destroyAllWindows()

# writer = cv2.VideoWriter(filename=)