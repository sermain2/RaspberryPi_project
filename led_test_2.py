 # RPi.GPIO 를 import 하고, 네임스페이스 RPi.GPIO 대신 GPIO 를 사용
import RPi.GPIO as GPIO

# GPIO 이름은 BCM 명칭 사용
# GPIO 23 출력으로 설정
# GPIO 24 출력으로 설정
# GPIO 18 입력으로 설정
# 메세지 화면 출력
GPIO.setmode( GPIO.BCM )
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.IN )
print ("Press SW or input Ctrl+C to quit")

# try:행과 아래 except KeyboardInterrupt: 
# 이하는 생략가능( GPIO warnning 방지 )
# 무한 반복문 - C 언어의 while(1)에 해당
# GPIO 23 에 LOW 출력( 적색 LED 소등 ) 
# GPIO 24 에 LOW 출력( 녹색 LED 소등 )
try:
  while True:
    GPIO.output(23, False)
    GPIO.output(24, False)
    # SW 가 ON 인 동안 반복
    # GPIO 23 에 HIGH 출력( 적색 LED 점등 ) 
    # GPIO 24 에 HIGH 출력( 녹색 LED 점등 )
    while GPIO.input(18) == 0:
      GPIO.output(23, True)
      GPIO.output(24, True)
      
# Ctrl-C 입력 시
# GPIO 관련설정 Clear
# 프로그램 종료 메세지 화면 출력      
except KeyboardInterrupt:
 GPIO.cleanup()
 print("bye~")
 
