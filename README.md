# RGB LED Matrix control with Raspberry Pi

This project allows you to connect to the led matrix via Raspberry Pi thanks to the Flask server and control it from a computer or mobile phone.


## Equipment



- <a href="https://rpishop.cz/s-raspberry-pi/3623-zonepi-sada-s-raspberry-pi-4-4gb-ram-32gb-karta-oficialni-krabicka-bila.html">Raspberry Pi 4 starter kit<a>
- <a href="https://rpishop.cz/rozsirujici-karty/1674-adafruit-rgb-matrix-hat-pro-raspberry-pi-mini-kit.html">Adafruit RGB Matrix HAT<a>
- <a href="https://rpishop.cz/led-displeje/1671-rgb-led-panel-32x64-mm.html?ssa_query=led">RGB LED Matrix – 32x64<a>
- <a href="https://rpishop.cz/zdroje/3664-sunny-21x55mm-5v4a-napajeci-zdroj-eu-cerna.html">Power supply 2,1x5,5 5V⎓4A<a>



## Setup Rapberry Pi

- <a href="https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up">Setting up your Raspberry Pi for first use<a>

- Install Git:
```
sudo apt update
sudo apt install git
```
- <a href="https://www.youtube.com/watch?v=3VrILb3dN0s&list=WL&index=9&t=8s">Download rgb-matrix software settings</a> from Henner Zeller:
```
curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh >rgb-matrix.sh
```
```
sudo bash rgb-matrix.sh
```

## Installation
Ensure you have python 3.6+ installed.
```bash
git clone <repo-url>
```
```bash
pip install -r requirements.txt
```

## Running the Server
```
python main.py
```

## Viewing The App

Go to `http://127.0.0.1:5000`