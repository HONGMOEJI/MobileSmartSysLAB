# led.py LED 출력을 위한 모듈

import time
import RPi.GPIO as GPIO

def init():
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)

def setInOut(pin, in_out):
	if in_out == "in":
		GPIO.setup(pin, GPIO.IN)
	if in_out == "out":
		GPIO.setup(pin, GPIO.OUT)

# pin에 연결된 LED에 value(0 / 1) 값을 주어 LED를 ON / OFF 하는 함수
def led_on_off(pin, value):
	GPIO.output(pin, value)


if __name__ == "__main__":
	init()
	on_off = 1 # 1은 디지털 출력 값. 1 = 5V
	led_pin = int(input("GPIO PIN을 입력하세요: "))
	setInOut(led_pin, "out")

	print("LED를 지켜 보세요.")

	# LED를 5번 깜박임
	for i in range(10):
		led_on_off(led_pin, on_off) # LED가 연결된 핀에 1(= 5V) 또는 0(= 0V) 인가
		time.sleep(1) # 1초 대기
		print(i, end = ' ', flush = True)
		on_off = 0 if on_off == 1 else 1 # 0과 1 토글링

	print()
	GPIO.cleanup()
