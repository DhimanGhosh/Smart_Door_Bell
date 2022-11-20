import RPi.GPIO as IO


class Pin:
    MOTION_SENSOR = 18
    PIEZZO_BUZZER = 12
    ULTRASONIC_ECHO = 13
    ULTRASONIC_TRIGGER = 23
    LED = 33

def GPIO_Pre_Setup():
    IO.setmode(IO.BOARD)
    IO.setwarnings(False)

def GPIO_Cleanup():
    IO.cleanup()
