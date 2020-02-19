![Version](https://img.shields.io/badge/Version-2.0-green)
[![Platform](https://img.shields.io/badge/Platform-Hassio-yellow)](https://www.home-assistant.io/hassio/installation/)
[![hassiohelp](https://img.shields.io/badge/Forum-hassiohelp-blue)](https://hassiohelp.eu/2019/12/21/termostato-programmabile/)

[![Telegram](https://img.shields.io/badge/Need-buttonTelegram-red)](https://hassiohelp.eu/2019/03/17/bot-telegram/)
![notNeed](https://img.shields.io/badge/notNeed-GoogleHome,Alexa-lightgrey)
![notNeed](https://img.shields.io/badge/notNeed-deviceTracker-lightgrey)

# Programmable thermostat from Telegram

![Lovelace](https://i.imgur.com/FcgOm4I.jpg)

## Versione 2.0
In this second version I added two operating modes:

- AWAY Mode (the reference temperature is off and set at 17 ° C, therefore as if it were manual, but with a different set Point temperature. The latter temperature can be changed by the automation)
- TurnOFF (I turn everything off, from climate to automation)

The package has been updated as well as the part of the telegram buttons and finally the lovelace part.

In detail.
An _input_boolean.away_mode_ has been added, which defines or not the away mode
In the first version, a history_stats sensor was introduced, referring to the period of heating of the radiators in the last 24 hours, that is to say yesterday.
Thus, from this sensor, the template was created, readable on a human level indicating _hh:mm:ss_.
With the update, another history_stats sensor has been added for a personal need.
This time the count is from midnight on the current day until the moment I request this value, _00:00 - now_ so to speak!
This also has its own template below, for a human vision.

The _uptime sensor_ and the two _binary_sensor_ used to know the cloud or MQTT mode of the **Shelly1** have been left unchanged, a device used as a clean contact for ignition and burial of the boiler.

### Telegram screens
| main screen | period thermo on |
|    --    |    --    |
|  ![buttonTelegram](https://i.imgur.com/OoW8bAY.jpg)  |  ![buttonTelegram](https://i.imgur.com/SqqB5ys.jpg)  |

## Version 1.0
The idea starts here (https://ledstripsandcode.blogspot.com/2018/11/simple-thermostat-scheduler-in-home.html), and then develops according to my needs.

I needed an hourly and daily / weekly program to manage the home heating, in addition to the simpler function of the thermostat (the boiler switches on below a certain temperature threshold).
In the specific of the program from Monday to Friday rather fixed times, fixed and the weekend, instead, two alternatives:

- radiators always off, since we are not at home
- always heated radiators, since we are always at home

So I thought of managing everything through two modes, **AUTO** and **MANUAL**.
- With **AUTO** there is an already preset scheduler (python script) where there are three programs:
  * the weekly one from Monday to Friday
  * that of the weekend when we are not at home
  * that of the weekend in which we are always present

- With **MANUAL**, on the other hand, the boiler switches on when the temperature drops below a setpoint temperature.

Finally, just for completeness, everything is managed remotely through the telegram "buttons", this because I have a 4G connection and as DuckDNS does not work in 4G.
So the only alternative to all this is Telegram!

### Telegram screens
| main screen | 
|    --    |
|  ![buttonTelegram](https://i.imgur.com/YElzPeB.jpg)  |

| auto mode | weekend mode | manual mode |
|    --    |    --    |    --    |
|  ![buttonTelegram](https://i.imgur.com/ujyeDNN.jpg)  | ![buttonTelegram](https://i.imgur.com/d4K77Z7.jpg) | ![buttonTelegram](https://i.imgur.com/v6j4F6M.jpg) |

