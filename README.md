# TMM4150: Machine Design and Mechatronics
## BattleBot: Datastream code and interface
This repo contains the code used to stream data from our battlebot to an external computer.



``Group 9``

### How to run the web-server:

1. Install Flask with pip:

```bash
pip install -U flask
```

2. From cmd run app.py (Make sure you are in the right directory)

```bash
python app.py
```

3. The cmd will tell you the address. (example: http://10.22.18.158:8044)

### How to run pi-side data-transmission:

1. Enter the correct directory:

```bash
cd tmm4150-g9/
```

2. Make sure you have a `config.py` placed in the `tmm4150-g9/pi-side` directory. This file must contain a variable called `serverAddress = "<serverIp>:<port>"`.

3. Install the [gpiozero](https://gpiozero.readthedocs.io/en/latest/) package via pip:

```bash
pip install -U gpiozero
```

4. Connect the pins correctly (see [this](https://gpiozero.readthedocs.io/en/latest/_images/pin_layout.svg) for an overview of Raspberry Pi pinout

| Pin | Reads |
|----------|----------|
| GPIO4 | Actuator state |
| GPIO18 | Compressor state |


5. Run the program (from `tmm4150-g9` folder)

```bash
python3 pi-side/main.py
```
