# Integrated Sensor Control module (ISC)

import time
import RPi.GPIO as GPIO
from adafruit_htu21d import HTU21D
import Adafruit_MCP3008
import busio
import CAM

# LED GPIO pin
led = 6 #GPIO6

# Ultrasonic GPIO pin
trig = 20 # GPIO20
echo = 16 # GPIO16

#
sda = 2 # GPIO2 핀. sda 이름이 붙여진 핀
scl = 3 # GPIO3 핀. scl 이름이 붙여진 핀

mcp = Adafruit_MCP3008.MCP3008(clk=11, cs=8, miso=9, mosi=10)

#
i2c = busio.I2C(scl, sda) # I2C 버스 통신을 실행하는 객체 생성
sensor = HTU21D(i2c) # I2C 버스에서 HTU21D 장치를 제어하는 객체 리턴


# GPIO init
def init():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # LED
    GPIO.setup(6, GPIO.OUT)

    # Ultrasonic
    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

# LED control
def controlLED(pin, value):
    GPIO.output(pin, value)


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

# Temp & Humidity sensor control
def getTemperature(sensor) : # 센서로부터 온도 값 수신 함수
    return float(sensor.temperature) # HTU21D 장치로부터 온도 값 읽기

def getHumidity(sensor) : # 센서로부터 습도 값 수신 함수
    return float(sensor.relative_humidity) # HTU21D 장치로부터 습도 값 읽기

# Photoresistor control
def getBrightness():
    brightness = mcp.read_adc(0)
    return brightness