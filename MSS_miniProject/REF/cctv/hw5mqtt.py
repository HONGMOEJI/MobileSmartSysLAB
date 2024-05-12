#publisher 

import io, time
import cv2
from PIL import Image, ImageFilter
import paho.mqtt.client as mqtt
import cv2
import CAM
import base64
import ISC


isStart  = False
isCamStart = False

def on_connect(client, userdata, msg, rc):
    client.subscribe("camera")
    client.subscribe("ISC")

def on_message(client, userdata, msg):
    global isStart
    global isCamStart

    if msg.topic == "ISC":
        if msg.payload.decode('utf-8') == 'start':
            isStart = True
            print("Start Monitoring")
        else:
            isStart = False

    if isStart and msg.payload.decode('utf-8') == 'camStart':
        isCamStart = True

    elif isStart and msg.payload.decode('utf-8') == 'camStop':
        isCamStart = False
        
    pass
        

broker_ip = "localhost"

client = mqtt.Client()
client.connect(broker_ip, 1883) # 1883 포트로 mosquitto에 접속
client.on_connect = on_connect
client.on_message = on_message

client.loop_start() # 메시지 루프를 실행하는 스레드 생성

CAM.init()
ISC.init()
stream = io.BytesIO()


while True:
    if isStart == True:
        countDistb = 0
        
        pastDistance = ISC.measureDistance()
        time.sleep(0.5)
        nowDistance = ISC.measureDistance()

        deltaDistance = abs(nowDistance - pastDistance)

        roomTemp = ISC.getTemperature(ISC.sensor)
        roomHumidity = ISC.getHumidity(ISC.sensor)

        roomLumi = ISC.getBrightness()

        client.publish("deltaDistance", deltaDistance, qos=0)
        client.publish("roomTemp", roomTemp, qos=0)
        client.publish("roomHumidity", roomHumidity, qos=0)
        client.publish("roomLumi", roomLumi, qos=0)
        
        if deltaDistance > 20:
            countDistb += 1
        if roomTemp > 22 or roomTemp < 18:
            countDistb += 1
        if roomHumidity > 60 or roomHumidity < 40:
            countDistb += 1
        if roomLumi > 400:
            countDistb += 1

        client.publish("sleepDistb", countDistb, qos=0)

        if isCamStart == True:
            frame = CAM.take_picture()
            stream.seek(0) # stream 파일의 커서를 맨 앞으로 이동한다
            image = Image.fromarray(frame) # numpy array 데이터를 PILLOW의 image 데이터 포맷으로 변환
            image.save(stream, format='JPEG') #이미지 변환후 JPEG 형식으로 이미지를 저장
            
            client.publish("image", stream.getvalue(), qos=0) # image토픽으로 이미지 데이터 전송
            stream.truncate() # stream 파일에 있는 모든 내용을 지운다
    else:
        print("I am idle")
        time.sleep(1)

camera.release() # 카메라 사용 끝내기
client.loop_stop() # 메시지 루프를 실행하는 스레드 종료
client.disconnect()
