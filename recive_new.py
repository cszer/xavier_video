import cv2
def receive():
    cap = cv2.VideoCapture('udpsrc port=5000 caps = "application/x-rtp, media=(string)video, clock-rate=(int)90000, encoding-name=(string)H264, payload=(int)96" ! rtph264depay ! decodebin ! videoconvert ! appsink', cv2.CAP_GSTREAMER)
    while True:
        ret,frame = cap_receive.read()
        print('frame recived')
        if not ret:
            print('empty frame')
recive()

