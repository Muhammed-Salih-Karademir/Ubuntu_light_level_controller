import cv2
import os
import time

#defines
genelToplam = 0
toplamR = 0
toplamG = 0
toplamB = 0
lightValue = 0.8
img = []
myMainMonitorName = ""
incLightCmd = ""
decLightCmd = ""
strlightValue = ""
cap = cv2.VideoCapture(0)
# TODO:video açılıp açılmadığnı check at
while(1):

    res,frame = cap.read()
    rows,cols,channels = frame.shape

    for i in range(rows):
        for j in range(cols):
                k = frame[i,j]
                toplamR += k[0]
                toplamG += k[1]
                toplamB += k[2]

    genelToplam=(toplamR + toplamG + toplamB)/3
    ortalama = genelToplam/(i*j)
    print(ortalama)
    f = os.popen('xrandr | grep " connected" | cut -f1 -d " "')
    aptSonuc = f.read()
    for i in aptSonuc:
        if "\n" in i:
            break
            myMainMonitorName +=i
#lightValue getirilmeli.
    print(myMainMonitorName)
    #print("xrandr --output " + myMainMonitorName + " --brightness %f" %lightValue)
    #myLightLevelCmd = "xrandr --output " + myMainMonitorName + " --brightness %f" %lightValue

    if ortalama >= 70 and lightValue < 1:
        lightValue += 0.1
        os.popen("xrandr --output eDP-1-1 --brightness %f"%lightValue)
    elif ortalama <= 70 and lightValue > 0.8:
        lightValue -= 0.1
        os.popen("xrandr --output eDP-1-1 --brightness %f"%lightValue)
    #cap.release()
    #cv2.destroyAllWindows()
    ortalama = 0
    genelToplam = 0
    toplamR = 0
    toplamG = 0
    toplamB = 0
    print(lightValue)
    #time.sleep(1)
