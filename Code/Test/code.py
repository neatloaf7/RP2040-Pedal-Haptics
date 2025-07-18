import board
import rotaryio
import digitalio
import time
import pwmio
from adafruit_motor import motor





##################################################################################

# Initialize Encoder 1
encoder1 = rotaryio.IncrementalEncoder(board.GP18, board.GP19)
last_position1 = encoder1.position

# Initialize Button 1
button1 = digitalio.DigitalInOut(board.GP6)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

#Initialize PWM
PWM_PIN_A = board.GP14
PWM_PIN_B = board.GP15
PWM_FREQ = 250
DECAY_MODE = motor.SLOW_DECAY

#Initialize DRV8871
pwm_a = pwmio.PWMOut(PWM_PIN_A, frequency=PWM_FREQ)
pwm_b = pwmio.PWMOut(PWM_PIN_B, frequency=PWM_FREQ)
motor1 = motor.DCMotor(pwm_a, pwm_b)
#motor1.decay_mode = DECAY_MODE

pwm = 0

while True:
    # Read Encoder 1
    position1 = encoder1.position
    position1_change = position1 - last_position1




    if position1 != last_position1:
        print("Encoder Change:", position1_change)
        last_position1 = position1
        if pwm < 255 and position1_change == 1:
            pwm = pwm + 1
        if pwm > 0 and position1_change == -1:
            pwm = pwm - 1
        print("pwm:", pwm)
    
    

    # Read Button 1
    if not button1.value:
        print("Button 1 Pressed")

    motor1.throttle = pwm/10
    pass
