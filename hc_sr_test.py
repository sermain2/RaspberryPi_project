# RPi.GPIO 클라스 import & 네임스페이스 GPIO 사용
# time 클라스 import
import RPi.GPIO as GPIO 
import time

# TRIG 변수에 핀번호 4 치환
# ECHO 변수에 핀번호 17 치환
TRIG = 19
ECHO = 26

# GPIO 명칭은 BCM SOC 핀 번호 사용
GPIO.setmode(GPIO.BCM)

# TRIG(GPIO19) 출력으로 설정
# ECHO(GPIO26) 입력으로 설정
# TRIG(GPIO19)로 LOW 출력
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
time.sleep(1) 
print ("Measure Distance with HC-SR04")

# 펄스폭 10us 펄스 출력 함수 trig()정의
# TRIG(GPIO19)로 HIGH 출력
# 10us 대기
# TRIG(GPIO19)로 LOW 출력, trig()정의 끝
def trig():
  GPIO.output(TRIG, True)
  time.sleep(0.000010)
  GPIO.output(TRIG, False)


# Echo 입력 HIGH 유지시간 반환함수 echo() 정의
# Echo 입력이 LOW 인동안
# echo_start 에 현재 시간 저장

def echo():
 while GPIO.input(ECHO) is 0:
  echo_start = time.time()

# Echo 입력이 HIGH 인동안
# echo_end 에 현재 시간 저장 

 while GPIO.input(ECHO) is 1:
  echo_end = time.time()

# echo_end 값과 echo_start 값의 차를 us 초단위로
# echo_us 에 저장
# echo_us 가 240 ~ 23000 범위에 있으면
# echo_us 값 반환
 
 echo_us = (echo_end - echo_start) * 1000000
 
 if(echo_us >= 240 and echo_us <= 23000):
  return echo_us

# 그렇지 않으면
# 0 반환, echo()정의 끝.
 
 else:
  return 0


# try: ~ except KeyboardInterrupt: 예외처리
# 무한루프 시작
# trig()함수 호출
# echo_time 에 echo()함수 반환값 저장
try:
 while True:
  trig()
  echo_time = echo()
  
  
  # echo_time 이 0 이 아니면
  # 측정거리 계산하여 dist 에 저장
  # dist 값 반올림하여 소수점이하 두자리까지 표시
  # dist 값 화면 출력
  if echo_time is not 0:
    dist = 17 * echo_time / 100
    dist = round(dist, 2)
    print ("Distance = ",dist,"(mm)")
    
    
  # echo_time 이 0 이면
  # 에러메세지 화면출력
  else:
    print ("Out of range")
 
  time.sleep(1);

# Ctrl+C 입력 예외 발생시
# GPIO.cleanup()함수 호출 
except KeyboardInterrupt:
 GPIO.cleanup()