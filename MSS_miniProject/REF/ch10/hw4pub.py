#publisher 

import io # 파일 I/O를 처리하기 위한 모듈
import cv2 # OpenCV 라이브러리
import time # 시간 관련 함수를 사용하기 위한 모듈
from PIL import Image, ImageFilter # Python Imaging Library, 이미지 처리를 위한 라이브러리
import paho.mqtt.client as mqtt # MQTT 프로토콜을 사용하기 위한 라이브러리

import led # LED 제어를 위한 모듈
import camera as CAM # 카메라 제어를 위한 모듈
import ultrasonic as US # 초음파 센서 제어를 위한 모듈

led.init() # == ultrasonic.init() # LED, Ultrasonic 센서를 이용하기 위한 GPIO 초기 설정
led.setInOut(6, "out") # 6번 핀을 출력 모드로 설정
led.setInOut(13, "out") # 13번 핀을 출력 모드로 설정
CAM.init() # 카메라 초기화
US.setTrigEcho() # 초음파 센서의 트리거와 에코 핀 설정

broker_ip = input("브로커의 IP를 입력하시오 >> ") # 브로커의 IP 주소 입력 받기

client = mqtt.Client() # MQTT 클라이언트 객체 생성
client.connect(broker_ip, 1883) # 1883 포트로 MQTT 브로커에 접속
client.loop_start() # MQTT 메시지 루프를 실행하는 스레드 생성

while True: # 무한 루프 시작
	distance = US.measureDistance() # 초음파 센서로 거리 측정

	if(distance < 20.0): # 거리가 20cm 미만이면
		led.led_on_off(13, 1) # RED LED 켜기
		led.led_on_off(6, 0) # GREEN LED 끄기
		print("도둑이 들어왔어요 !!!! (%fcm)" % distance) # 메시지 출력
		frame = CAM.take_picture() # 카메라로 사진 찍기
		pilim = Image.fromarray(frame) # OpenCV의 프레임을 PIL 이미지로 변환
		stream = io.BytesIO() # 이미지를 저장할 바이트 형태의 스트림 버퍼 생성
		pilim.save(stream, 'jpeg') # 프레임을 jpeg 형태로 바꾸어 스트림에 저장
		im_bytes = stream.getvalue() # 스트림의 내용을 바이트 배열로 저장
		client.publish("jpeg", im_bytes, qos = 0) # 이미지 데이터를 "jpeg" 토픽으로 전송
		client.publish("msg", 1, qos = 0) # 메시지를 "msg" 토픽으로 전송
	else:
		led.led_on_off(13, 0) # RED LED 끄기
		led.led_on_off(6, 1) # GREEN LED 켜기
		print("아무 일도 없어요!") # 메시지 출력
		client.publish("msg", 0, qos=0) # 메시지를 "msg" 토픽으로 전송

	time.sleep(1) # 1초 동안 대기


CAM.final() # 카메라 사용 종료
client.loop_stop() # MQTT 메시지 루프를 실행하는 스레드 종료
client.disconnect() # MQTT 브로커 연결 종료

