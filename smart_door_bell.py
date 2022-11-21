import time
from config import *


class SmartDoorBell:
    def __init__(self) -> None:
        """
        Constructor to initialize the GPIO pins for various components used
        """
        self.motion = Pin()['MOTION_SENSOR']
        self.buz = Pin()['PIEZZO_BUZZER']
        self.echo = Pin()['ULTRASONIC_ECHO']
        self.trig = Pin()['ULTRASONIC_TRIGGER']
        self.led = Pin()['LED']

        self.__setup()

    def __setup(self) -> None:
        """
        Perform GPIO pre-setup and inidividual components
        """
        GPIO().pre_setup()
        
        Component(self.motion).setup('in')
        Component(self.buz).setup('out')
        Component(self.led).setup('out')
        
        Component(self.echo).setup('in')
        Component(self.trig).setup('out')

    def __distance(self) -> float:
        """
        Calculate the distance from Ultrasonic Sensor to Object
        
        :return: float distance
        """
        Component(self.trig).on()

        time.sleep(0.00001)
        Component(self.trig).off()

        StartTime = time.time()
        StopTime = time.time()

        while Component(self.echo).input_detected() == 0:
            StartTime = time.time()

        while Component(self.echo).input_detected() == 1:
            StopTime = time.time()

        TimeElapsed = StopTime - StartTime
        distance = (TimeElapsed * 34300) / 2

        return distance

    def __destroy(self) -> None:
        """
        Cleanup all the GPIO Pins
        """
        GPIO().cleanup()

    def __play_piezo_buzzer_with_led(self) -> None:
        """
        Pulsed play Piezzo Buzzer along with LED
        """
        dur = .1
        for _ in range(10):
            Component(self.buz).on()
            Component(self.led).on()
            
            time.sleep(dur)
            
            Component(self.buz).off()
            Component(self.led).off()
            
            time.sleep(dur)

    def motion_detect_door_bell(self) -> None:
        """
        Main code to play buzzer and turn on led when hand is waved at less than 10cm away from ultrasonic sensor 
        """
        try:
            time.sleep(2)
            while True:
                if Component(self.motion).input_detected():
                    distance = self.__distance()
                    if distance < 10.0:
                        text = f'Movement Detected at {distance:.1f} cm away'
                        print(text)
                        self.__play_piezo_buzzer_with_led()
                        time.sleep(2)
                time.sleep(.1)
        except:
            self.__destroy()
