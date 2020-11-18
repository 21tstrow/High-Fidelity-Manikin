from gpiozero import LED
from time import sleep 

##left_hand_led_one = LED(16)
##left_hand_led_two = LED(20)
right_hand_led_one = LED(16)
right_hand_led_two = LED(20)
mouth_led= LED(26)

def mouth_led_on(on):
  if on:
    mouth_led.on()
  else:
    mouth_led.off()

'''
def lefthand_led_on(left_on):
  if left_on:
    left_hand_led_one.on()
    left_hand_led_two.on()
  else:
    left_hand_led_one.off()
    left_hand_led_two.off()
'''

def righthand_led_on(right_on):
  if right_on:
    right_hand_led_one.on()
    right_hand_led_two.on()
  else:
    right_hand_led_one.off()
    right_hand_led_two.off()
