from machine import Pin, PWM, ADC
from time import sleep

pot = ADC(Pin(34, Pin.IN),atten=3) # atten 3 = 11db attentuation (150mV - 2450mV)
pot.atten(ADC.ATTN_11DB) # 11dB attenuation (150mV - 2450mV)
pot.width(ADC.WIDTH_12BIT) # Bestememr opløsningen i bits 12'

IN1 = Pin(21,Pin.OUT)
IN2 = Pin(22,Pin.OUT)
IN3 = Pin(32,Pin.OUT)
IN4 = Pin(33,Pin.OUT)
pb1 = Pin(4, Pin.IN)
pb2 = Pin(0, Pin.IN)

pins = [IN1, IN2, IN3, IN4]

sequence = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
sequence_CCW = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]


## loop til at gå den ene vej
# while True:
#     for step in sequence:
#         for i in range(len(pins)):
#             pins[i].value(step[i])
#             sleep(0.001)

## Loop til en stepper motor, når jeg trykker på en af knapperne på educaboard, går den hver sin vej.
# while True:
#     if pb1.value() == 0:
#          for step in sequence:
#             for i in range(len(pins)):
#                 pins[i].value(step[i])
#                 sleep(0.001)
#     elif pb2.value() == 0:
#          for step in sequence_CCW:
#             for i in range(len(pins)):
#                 pins[i].value(step[i])
#                 sleep(0.001)
                


## Loop til stepper motor, potmeter
while True: #starter uendligt loop
    pot_value = pot.read() #gemmer aflæsning af ADC objektets read metode i variablen pot_val
    if pot_value >= 100:
        for step in sequence:
            for i in range(len(pins)):
                pins[i].value(step[i])
                sleep(0.001)
    elif pot_value <= 100:
        for step in sequence_CCW:
            for i in range(len(pins)):
                pins[i].value(step[i])
                sleep(0.001)
        
