import RPi.GPIO as GPIO
from time import sleep
import os

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

funcs = {
  "F1": "MCDU_KB_12", "F2": "MCDU_KB_13", "F3": "MCDU_KB_20", "F4": "MCDU_KB_21", "F5": "MCDU_KB_22", "F6": "null", "F7": "null", "F8": "MCDU_KB_14", "F9": "MCDU_KB_15",
  "F10": "MCDU_KB_23", "F11": "MCDU_KB_24", "F12": "null", "F13": "MCDU_KB_26", "F14": "null", "F15": "MCDU_KB_16", "F16": "null", "UP": "MCDU_KB_17", "DOWN": "MCDU_KB_19",
  "LEFT": "MCDU_KB_25", "RIGHT": "MCDU_KB_18", "0": "MCDU_KB_27", "1": "MCDU_KB_28", "2": "MCDU_KB_29", "3": "MCDU_KB_30", "4": "MCDU_KB_31", "5": "MCDU_KB_32", "6": "MCDU_KB_33",
  "7": "MCDU_KB_34", "8": "MCDU_KB_35", "9": "MCDU_KB_36", "DOT": "MCDU_KB_37", "PLUS": "MCDU_KB_65", "A": "MCDU_KB_39", "B": "MCDU_KB_40", "C": "MCDU_KB_41", "D": "MCDU_KB_42",
  "E": "MCDU_KB_43", "F": "MCDU_KB_44", "G": "MCDU_KB_45", "H": "MCDU_KB_46", "I": "MCDU_KB_47", "J": "MCDU_KB_48", "K": "MCDU_KB_49", "L": "MCDU_KB_50", "M": "MCDU_KB_51",
  "N": "MCDU_KB_52", "O": "MCDU_KB_53", "P": "MCDU_KB_54", "Q": "MCDU_KB_55", "R": "MCDU_KB_56", "S": "MCDU_KB_57", "T": "MCDU_KB_58", "U": "MCDU_KB_59", "V": "MCDU_KB_60", "X": "MCDU_KB_62",
  "W": "MCDU_KB_61", "Y": "MCDU_KB_63", "Z": "MCDU_KB_64", "OVFY": "MCDU_KB_67", "CLR": "MCDU_KB_68", "SL1": "MCDU_KB_00", "SL2": "MCDU_KB_01", "SL3": "MCDU_KB_02", "SL4": "MCDU_KB_03",
  "SL5": "MCDU_KB_04", "SL6": "MCDU_KB_05", "SR1": "MCDU_KB_06", "SR2": "MCDU_KB_07", "SR3": "MCDU_KB_08", "SR4": "MCDU_KB_09", "SR5": "MCDU_KB_10", "SR6": "MCDU_KB_11", "SLASH": "MCDU_KB_38",
  "SP": "MCDU_KB_66"
}

for p in range(9):
    GPIO.setup(COLUNA[p],GPIO.OUT)
    GPIO.output(COLUNA[p], 1)

for h in range(9):
    GPIO.setup(LINHA[h], GPIO.IN, pull_up_down = GPIO.PUD_UP)

def url_call(button):
    call = "curl -s http://192.168.1.105:4040/MCDU/" + funcs[button]
    os.system(call)

try:
    while(True):
        for m in range(9):
            GPIO.output(COLUNA[m],0)

            for g in range(9):
                if GPIO.input(LINHA[g]) == 0:
		    url_call(COMANDOS[g][m])

                    while (GPIO.input(LINHA[g]) == 0):
                        pass
                    sleep(0.3)

            GPIO.output(COLUNA[m],1)

except KeyboardInterrupt:
    GPIO.cleanup()
