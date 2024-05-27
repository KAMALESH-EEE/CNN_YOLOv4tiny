import cv2
#import serial


#ser = serial.Serial('COM6', 9600)

c=0
d=0

net = cv2.dnn.readNet("code/yolov4-tiny-custom_final.weights", "code/yolov4-tiny-custom.cfg")#D:\Robotics\code\MARS_2_main.py
model = cv2.dnn_DetectionModel(net)

model.setInputParams(size =(224,224), scale = 1/255)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640 )
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480 )


Class = ["Healthy","Defect"]

def detect():   
    global d
    
    ret, frame = cap.read()
    
    area=0
    f= False
    (class_ids, scores, bboxes) = model.detect(frame)

    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        print( w, h)
        if(score > 0.75):
            f =True
            d+=1
            cv2.putText(frame,str(Class[class_id]) ,(x, y-5), cv2.FONT_HERSHEY_PLAIN, 2, (10, 0, 250), 2)
            cv2.rectangle(frame, (x,y),(x+w, y+h), (255,255,255), 2)
            if((area < h*w) and class_id == 1 ):
                  area = int(h*w)
    
    cv2.imshow("Frame", frame)
    cv2.waitKey(1)
    if(f):
        return area
    else:
         return 0

while True:
    a = detect()
    print (a)
    if(a>500):
        c=c+1
        cv2.waitKey(0)
         
