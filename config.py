import RPi.GPIO as IO


class Pin:
    MOTION_SENSOR = 18
    PIEZZO_BUZZER = 12
    ULTRASONIC_ECHO = 13
    ULTRASONIC_TRIGGER = 23
    LED = 33

def components_setup(component_pin: int, mode):
    if mode.lower() == 'in':
        IO.setup(component_pin, IO.IN)
    else:
        IO.setup(component_pin, IO.OUT)

def components_input(component_pin: int):
    return IO.input(component_pin)

def components_output(component_pin: int, mode: bool):
    if mode:
        IO.output(component_pin, True)
    else:
        IO.output(component_pin, False)

def GPIO_Pre_Setup():
    IO.setmode(IO.BOARD)
    IO.setwarnings(False)

def GPIO_Cleanup():
    IO.cleanup()
