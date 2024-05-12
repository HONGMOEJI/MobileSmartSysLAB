# ultrasonic.py 초음파 센서를 이용하기 위한 모듈

import time
import RPi.GPIO as GPIO

trig = 20 # GPIO20
echo = 16 # GPIO16

def init(): # initialization
    GPIO.setmode(GPIO.BCM)  
    GPIO.setwarnings(False)
  
def setTrigEcho(ltrig = 20, lecho = 16):
    global trig, echo
    trig = ltrig
    echo = lecho
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)
def measureDistance():
  GPIO.output(trig, 1) # tr
  GPIO.output(trig, 0) # trig 핀 신호 High -> Low 초음파 발사 지시
  while(GPIO.input(echo) == 0): # echo 핀 값이 1로 바뀔 때까지 루프
    pass

# echo 핀 값이 1이면 초음파가 발사되었음
  pulse_start = time.time() # 초음파 발사 시간 기록
  while(GPIO.input(echo) == 1): # echo 핀 값이 0이 될 때까지 루프
    pass
# echo 핀 값이 0이 되면 초음파를 수신하였음
  pulse_end = time.time()
  pulse_duration = pulse_end - pulse_start # 경과 시간 계산
  return pulse_duration*340*100/2 # 거리 계산 (cm)
 
if __name__ == "__main__":
  init()
  setTrigEcho()
  while True:
    distance = measureDistance()
    time.sleep(0.5)
    print("물체와의 거리는 %fcm 입니다." %distance)
    pass
