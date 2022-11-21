import RPi.GPIO as IO
import configparser


class Pin:
    def __init__(self):
        self.__parser = configparser.ConfigParser()
        self.__config_file = 'config.ini'
        self.__component_pin = {}

        self.__parse_config()

    def __parse_config(self):
        self.__parser.read(self.__config_file)
        for sect in self.__parser.sections():
            if sect == 'Pin':
                for k, v in self.__parser.items(sect):
                    self.__component_pin[k.upper()] = int(v)

    def __getitem__(self, item):
        return self.__component_pin[item]

class Component:
    def __init__(self, component_pin: int):
        self.__pin = component_pin

    def on(self):
        IO.output(self.__pin, True)

    def off(self):
        IO.output(self.__pin, False)

    def setup(self, mode: str):
        if mode.lower() == 'in' or mode.lower() == 'i':
            IO.setup(self.__pin, IO.IN)
        elif mode.lower() == 'out' or mode.lower() == 'o':
            IO.setup(self.__pin, IO.OUT)

    def input_detected(self):
        return IO.input(self.__pin)


class GPIO:
    def __init__(self, mode=IO.BOARD):
        self.__mode = mode
    
    def pre_setup(self):
        IO.setmode(self.__mode)
        IO.setwarnings(False)

    def cleanup(self):
        IO.cleanup()
