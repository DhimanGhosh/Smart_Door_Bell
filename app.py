import RPi.GPIO as IO
import time
import config
from pi_speak import speak


class Smart_Door_Bell:
    def __init__(self) -> None:
        self.motion_sensor_PIN = config.Pin.MOTION_SENSOR
        self.piezzo_buzzer_PIN = config.Pin.PIEZZO_BUZZER
        self.ultrasonic_echo_PIN = config.Pin.ULTRASONIC_ECHO
        self.ultrasonic_trigger_PIN = config.Pin.ULTRASONIC_TRIGGER
        self.led_PIN = config.Pin.LED

        self.__setup()

    def __setup(self):
        config.GPIO_Pre_Setup()

        IO.setup(self.motion_sensor_PIN, IO.IN)
        IO.setup(self.piezzo_buzzer_PIN, IO.OUT)

        IO.setup(self.ultrasonic_echo_PIN, IO.IN)
        IO.setup(self.ultrasonic_trigger_PIN, IO.OUT)

        IO.setup(self.led_PIN, IO.OUT)

    def __distance(self):
        # set Trigger to HIGH
        IO.output(self.ultrasonic_trigger_PIN, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        IO.output(self.ultrasonic_trigger_PIN, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while IO.input(self.ultrasonic_echo_PIN) == 0:
            StartTime = time.time()

        # save time of arrival
        while IO.input(self.ultrasonic_echo_PIN) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s) and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        return distance

    def __destroy(self):
        config.GPIO_Cleanup()

    def __play_piezo_buzzer_with_led(self):
        dur = .1
        for _ in range(10):
            IO.output(self.piezzo_buzzer_PIN, True)
            IO.output(self.led_PIN, True)
            time.sleep(dur)
            IO.output(self.piezzo_buzzer_PIN, False)
            IO.output(self.led_PIN, False)
            time.sleep(dur)

    def motion_detect_door_bell(self):
        try:
            time.sleep(2)
            while True:
                print('waiting for motion!')
                if IO.input(self.motion_sensor_PIN):
                    print('motion detected!')
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
    alarm = Smart_Door_Bell()
    alarm.motion_detect_door_bell()