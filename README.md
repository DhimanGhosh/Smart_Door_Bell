# Smart_Door_Bell

## Components
#### Required
- Raspberry Pi 4B (any version will support)
- Micro SD Card
- HC-SR04
- PIR Motion Sensor
- Piezzo Buzzer
- Jumper Cables
#### Optional
- LED
- 47 Ohm Registor
- Breadboard
- WiFi / Ethernet
- Mouse
- Keyboard
- Monitor
- Micro HDMI to HDMI cable

## Setup
> Note: x = y means 'x' is the label on sensor / components, 'y' os the connection to Raspberyr Pi Pins

| Component | Pins Arrangement |
| ------ | ------ |
| PIR Motion Sensor | +5V=5V0, OUT=Pin18, GND=GND |
| HC-SR04 | Vcc=5V0, Trig=Pin23, Echo=Pin13, Gnd=GND |
| Piezzo Buzzer | Black=GND, Red=Pin12 |
| LED | Anode=Registor+Pin33, Cathod=GND |

## Execute
> Note: Edit [config.ini](https://github.com/DhimanGhosh/Smart_Door_Bell/blob/main/config.ini) and enter the GPIO pins of your setup (setup as Pin Numbering)
```sh
chmod +x run.sh
./run.sh
```
