import pyautogui
import numpy as np
import cv2

resolution = pyautogui.size()

codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording.avi"

fps = 60.00

out =  cv2.VideoWriter(filename,codec,fps,resolution)

cv2.namedWindow("live",cv2.WINDOW_NORMAL)

cv2.resizeWindow("Live",480,270)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    out.write(frame)

    cv2.imshow("Live",frame)
    if cv2.waitKey(1) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()