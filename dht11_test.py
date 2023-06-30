# RPi.GPIO import & 네임스페이스 GPIO 사용
# 'time' 클라스 멤버 중 'sleep' import
# './DHT11_Python/dht11.py'를 import 하고,
# 네임스페이스로 'dht11'을 사용.

import RPi.GPIO as GPIO
from time import sleep 
import DHT11_Python.dht11 as dht11

GPIO.setmode(GPIO.BCM)

# dht11 인스턴스 생성
print ("Get temperature & humidity from dht11")
dht = dht11.DHT11(pin=4)

# try: ~ except…: 에외처리
# 무한 반복 시작
# result 에 dht11 센서 측정값 저장
try:
 while True:
  result = dht.read()

# result 에 저장된 측정값이 유효한 값이면
# 측정 온도 화면출력
# 측정 습도 화면출력
 
  if result.is_valid():
    print("T = %-3.1f C" % result.temperature)
    print("H = %-3.1f %%" % result.humidity)
 
  sleep(6)

# Ctrl+C 가 입력되면
# GPIO.cleanup() 호출 
except KeyboardInterrupt:
 GPIO.cleanup()