from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui
import datetime


screen_size = pyautogui.size()

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
time_stamp = datetime.datetime.now().strftime("%d-%m-%Y %H-%M-%S")
out = cv2.VideoWriter(f"{time_stamp}.mp4", fourcc, 20, (screen_size.width, screen_size.height))

# webcam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0, 0, screen_size.width, screen_size.height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    # _, frame = webcam.read()
    # fr_height, fr_width, _ = frame.shape
    # img_final[0:fr_height, 0:fr_width, :] = frame[0:fr_height, 0:fr_width, :]
    cv2.imshow("Capture", img_final)
    # cv2.imshow('Webcam', frame)
    out.write(img_final)

    if cv2.waitKey(10) == ord('q'):
        break

