# RPi.GPIO 를 import 하고 네임스페이스는 GPIO 를사용
# time 에 정의된 기능을 사용( time.sleep 
import RPi.GPIO as GPIO
import time

# GPIO 이름은 BCM 명칭 사용
# GPIO 23 출력으로 설정
# GPIO 24 출력으로 설정
# ""안의 문자열 화면 출력
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
print ("GPIO Test~, press Ctrl+C to quit")

# 'try:' + 'except..' 에러처리
# 무한 반복 'while'문( C 언어 – 'while(1)' )
# GPIO 23 에 HIGH 출력( 적색 LED 점등 ) 
# GPIO 24 에 HIGH 출력( 녹색 LED 점등 )
# 0.5 초 동안 대기
try:
  while True:
    GPIO.output(23, True )
    GPIO.output(24, True )
    time.sleep(0.5)
 
# GPIO 23 에 LOW 출력( 적색 LED 소등 ) 
# GPIO 24 에 LOW 출력( 녹색 LED 소등 )
# 0.5 초 동안 대기 ( 여기까지 반복 )
    GPIO.output(23, False)
    GPIO.output(24, False)
    time.sleep(0.5)
 
# Ctrl-C 입력 발생 시
# GPIO 관련설정 Clear
# 프로그램 종료 메세지 화면 출력
 
except KeyboardInterrupt:
  GPIO.cleanup()
  print ("bye~")