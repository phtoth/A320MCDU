import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LINHA = [2,3,4,17,27,22,10,9,11]
COLUNA = [14,15,18,23,24,25,8,12,16]

for p in range(9):
    GPIO.setup(COLUNA[p],GPIO.OUT)
    GPIO.output(COLUNA[p], 1)

for h in range(9):
    GPIO.setup(LINHA[h], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while(True):
        for m in range(9):
            GPIO.output(COLUNA[m],0)
            
            for g in range(9):
                if GPIO.input(LINHA[g]) == 0:
                    print "Foi"
                    print  LINHA[g], COLUNA[m]
                    while (GPIO.input(LINHA[g]) == 0):
                        pass
                    sleep(0.3)
            GPIO.output(COLUNA[m],1)

except KeyboardInterrupt:
    GPIO.cleanup()
