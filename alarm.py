import cv2
import threading
import winsound
capture=cv2.VideoCapture(0) #videocamera da dove registare
capture.set(cv2.CAP_PROP_FRAME_WIDTH,640) #dimensioni
capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480) #dimensioni
_, frame1=capture.read() #variabile a cui mandare info telecamera
frame1=cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

alarm=False
alarm_mode=False
alarm_counter=0
def allarme_rumore():
    global alarm
    while alarm_mode == True:
        winsound.Beep(2500,1000) ## suono
    alarm=False

while True:
    
    _, frame2=capture.read()

    if alarm_mode == True: #moalità allarme
        frame_bw=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        difference=cv2.absdiff(frame_bw,frame1)#differenze
        threshold=cv2.threshold(difference,25,255,cv2.THRESH_BINARY)[1]
        frame1=frame_bw

        if threshold.sum()>1:
            alarm_counter+=1
        cv2.imshow("ALARM",threshold)#finestra visualizzazione nero
    else:
        cv2.imshow("CAMERA",frame2)#finestra visualizzazione normale
    
    if alarm_counter >10:
        if alarm==False:
            alarm=True
            threading.Thread(target=allarme_rumore).start()

    press=cv2.waitKey(30)
    if press==ord("t"):
        if alarm_mode == True:
            alarm_mode=False
        else:
            alarm_mode=True
        alarm_counter=0

    if press==ord("q"):
        break
print("alarm counter",alarm_counter)
capture.release()
cv2.destroyAllWindows