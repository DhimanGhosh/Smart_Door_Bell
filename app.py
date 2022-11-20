import time
from config import *
from pi_speak import speak


class SmartDoorBell:
    def __init__(self) -> None:
        self.motion_sensor_PIN = Pin.MOTION_SENSOR
        self.piezzo_buzzer_PIN = Pin.PIEZZO_BUZZER
        self.ultrasonic_echo_PIN = Pin.ULTRASONIC_ECHO
        self.ultrasonic_trigger_PIN = Pin.ULTRASONIC_TRIGGER
        self.led_PIN = Pin.LED

        self.__setup()

    def __setup(self):
        GPIO_Pre_Setup()
        
        components_setup(self.motion_sensor_PIN, 'in')
        components_setup(self.piezzo_buzzer_PIN, 'out')
        
        components_setup(self.ultrasonic_echo_PIN, 'in')
        components_setup(self.ultrasonic_trigger_PIN, 'out')
        
        components_setup(self.led_PIN, 'out')

    def __distance(self):
        # set Trigger to HIGH
        components_output(self.ultrasonic_trigger_PIN, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        components_output(self.ultrasonic_trigger_PIN, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while components_input(self.ultrasonic_echo_PIN) == 0:
            StartTime = time.time()

        # save time of arrival
        while components_input(self.ultrasonic_echo_PIN) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s) and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance

    def __destroy(self):
        GPIO_Cleanup()

    def __play_piezo_buzzer_with_led(self):
        dur = .1
        for _ in range(10):
            components_output(self.piezzo_buzzer_PIN, True)
            components_output(self.led_PIN, True)
            time.sleep(dur)
            components_output(self.piezzo_buzzer_PIN, False)
            components_output(self.led_PIN, False)
            time.sleep(dur)

    def motion_detect_door_bell(self):
        try:
            time.sleep(2)
            while True:
                if components_input(self.motion_sensor_PIN):
                    distance = self.__distance()
                    if distance < 10.0:
                        text = f'Movement Detected at {distance:.1f} cm away'
                        print(text)
                        # speak(text)
                        self.__play_piezo_buzzer_with_led()
                        time.sleep(2)
                time.sleep(.1)
        except:
            self.__destroy()


if __name__ == '__main__':
    alarm = SmartDoorBell()
    alarm.motion_detect_door_bell()
