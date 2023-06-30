# RPi.GPIO 를 import 하고, 네임스페이스 RPi.GPIO 대신 GPIO 를 사용
# GPIO 이름은 BCM 명칭 사용

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# GPIO 23 출력으로 설정
# GPIO 24 출력으로 설정
# GPIO 18 입력으로 설정
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(18, GPIO.IN )

# GPIO 23 에 LOW 출력( 적색 LED 소등 )
# GPIO 24 에 LOW 출력( 녹색 LED 소등 )
# 메세지 화면 출력
GPIO.output(23, False)
GPIO.output(24, False)
print ("PIR Sensor Test")


# try: except KeyboardInterrupt: 에러처리
# 무한 반복 구간 - C 언어의 while(1)에 해당
# GPIO 18 입력(센서 출력)이 LOW 이면
# GPIO 23 에 LOW 출력( 적색 LED 소등 )
# GPIO 24 에 HIGH 출력( 녹색 LED 점등 )
try:
  while True:
    if GPIO.input(18) == 0:
      GPIO.output(23, False)
      GPIO.output(24, True )
    # GPIO 18 입력(센서 출력)이 HIGH 이면
    # GPIO 23 에 HIGH 출력( 적색 LED 점등 ) 
    # GPIO 24 에 LOW 출력( 녹색 LED 소등 )  
    else:
      GPIO.output(23, False)
      GPIO.output(24, True )
      
# Ctrl-C 입력 시
# GPIO 관련설정 Clear      
except KeyboardInterrupt:
 GPIO.cleanup()