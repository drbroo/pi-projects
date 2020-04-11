#!/usr/bin/env python3
########################################################################
# Filename    : Blink.py
# Description : Basic usage of GPIO. Let led blink.
# auther      : www.freenove.com
# modification: 2019/12/26
########################################################################
from gpiozero import LED
from time import sleep

print ('Program is starting ... ')

leds_at = [12,16,20,21] #physical 32, 36, 38,40 on header
led = list()

for index in range(len(leds_at)):
    led.append(LED(leds_at[index]))         

which_on = 0
delay = 0.25
delay_inc = 0.006

while True:
    led[which_on].on()
    sleep(delay)
    delay *= (1-delay_inc)
    led[which_on].off()
    which_on = (which_on + 1) % len(leds_at)

