import cv2 as cv
from windowcapture import WindowCapture
import brain
from keyinput import PressKey#https://gist.github.com/tracend/912308
import keyboard
import numpy as np
windowcap = WindowCapture("Trackmania")

recording=True
scaledw=40
scaledh=int(9/16*scaledw)
saved_actions=np.zeros(4+scaledw*scaledh) #= [2,2,2,2]#np.zeros(shape=[0,4],dtype=np.int)

while(True):
    screenshot = windowcap.get_screenshot()
    resized = cv.resize(screenshot,(scaledw,scaledh),interpolation=cv.INTER_AREA)
    grayscale = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)
    cv.imshow("screen grab",grayscale)
    if recording:
        action = [int(keyboard.is_pressed('w')),int(keyboard.is_pressed('a')),int(keyboard.is_pressed('s')),int(keyboard.is_pressed('d'))]
        if(abs(np.max(action))>1):
            continue
        #the action and screenshot for each frame are a one dimensional array, with the first four numbers being the elements and the remaining elments being the flattened array of pixels from the screenshot
        saved_actions= np.vstack((saved_actions,np.append(action,np.reshape(grayscale,(scaledw*scaledh)))))
    else:
        actions = brain.process(screenshot)
        if actions[0]:#W
            PressKey(0x11)
        if actions[1]:#A
            PressKey(0x1E)
        if actions[2]:#S
            PressKey(0x1F)
        if actions[3]:#D
            PressKey(0x20)

    if cv.waitKey(1) == ord('q') or keyboard.is_pressed("q"):
        cv.destroyAllWindows()
        break
print(saved_actions[1:])
np.save("data.npy",saved_actions[1:])
print(np.load("data.npy"))


