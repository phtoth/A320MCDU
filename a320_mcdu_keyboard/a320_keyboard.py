import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

LINHA = [2,3,4,17,27,22,10,9,11]
COLUNA = [14,15,18,23,24,25,8,12,16]

COMANDOS = [['F1','F2','F3','F4','F5','F6','F7','F15','F16'],
            ['F8','F9','F10','F11','F12','F13','F14','LEFT','UP'],
            ['A','B','C','D','E','RIGHT','DOWN','1','2'],
            ['3','F','G','H','I','J','4','5','6'],
            ['7','8','9','DOT','0','PLUS','K','L','M'],
            ['N','O','P','Q','R','S','T','U','V'],
            ['W','X','Y','SL1','SL2','SL3','SL4','SL5','SL6'],
            ['Z','SLASH','SP','SR1','SR2','SR3','SR4','SR5','SR6'],
            ['OVFY','CLR']]

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
                    print  COMANDOS[g][m]
                    while (GPIO.input(LINHA[g]) == 0):
                        pass
                    sleep(0.3)
            GPIO.output(COLUNA[m],1)

except KeyboardInterrupt:
    GPIO.cleanup()
