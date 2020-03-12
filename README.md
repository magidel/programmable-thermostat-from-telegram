![Version](https://img.shields.io/badge/Version-3.5-green)
[![Platform](https://img.shields.io/badge/Platform-Hassio-yellow)](https://www.home-assistant.io/hassio/installation/)
[![hassiohelp](https://img.shields.io/badge/Forum-hassiohelp-blue)](https://hassiohelp.eu/2019/12/21/termostato-programmabile/)

[![Telegram](https://img.shields.io/badge/Need-buttonTelegram-red)](https://hassiohelp.eu/2019/03/17/bot-telegram/)
![notNeed](https://img.shields.io/badge/notNeed-GoogleHome,Alexa-lightgrey)
![notNeed](https://img.shields.io/badge/notNeed-deviceTracker-lightgrey)

# Programmable thermostat from Telegram

## Versione 3.5
Mostly bug fixes !!
I wanted to fix some flaws:

- #### Initialization of input_boolean ("auto_mode" and "weekend_on").
  This involved the automatic ignition of the boiler at each restart, if hassio was in MANUAL mode.
  Restarted in AUTO mode did not happen.


- #### Delete Climate.target_temp 
  In the definition of the climate entity I have eliminated "target_temp".
  In the above case it imposed its initialisation temperature, "disturbing" the MANUAL mode.
  No problem because when choosing a mode the reference temperature will be set directly from the mode itself.


- #### Automation "alias: Thermo Start"
  I eliminated the first automation, the one that forced input_boolean.auto_mode = "ON" when starting Hassio.
  Now the system restarts leaving the previously chosen mode unchanged.


- #### Automation "alias: Thermo AUTO Mode"
  Unlike before, the initial state is now OFF.
  There is no longer the "homeassistant start" option in the trigger.


- #### Automation "Thermo MANUAL Mode"
  The initial OFF state remains.
  In the trigger, input_boolean.auto_mode OFF has been deleted.
  The python_script.scheduler_manual is no longer launched, but the action sets the reference temperature directly, therefore one script less !!!
  Moreover, it was useless as summing up the script only set the temperature of the climate entity, unlike the AUTO script which had set days and times.


- #### Automation "alias: Thermo AUTO Mode", "alias: Thermo AWAY Mode", "alias: Thermo MANUAL Mode"
  In previous versions I have privileged the interface of Telegram buttons.
  In this version I have dedicated myself to Lovelace's own interface.
  With these 3 automations I indicate what to enable and what to disable between input_boolean and automations when I enable or disable the mode switches from the UI.


- #### Automation "alias: BoostSetPoint"
  I realized that the BoostSetPoint automations had the same alias.
  Now they are called "BoostSetPointIncrement" and "BoostSetPointDecrement".



## Versione 3.0
In this third version I added:
- input_text to view the activated mode (AUTO, MANUAL, AWAY)
- Boost mode, increase HighTarget in AUTO mode by +0.5°C from 19.00 to 08.00 everyday (temperature increase for my wife ;) )
- I fixed the lovelace UI:
![Lovelace](https://i.imgur.com/uB6txID.jpg)

In the lovelace UI one mode excludes the other with relative notification on telegram:

![Notification](https://i.imgur.com/EbVYXDp.jpg)

In addition, an automation activates the AUTO mode when Hassio starts.
The modality can be changed through Telegram or the Lovelace UI.

### Telegram screens
| main screen | AUTO mode |
|    --    |    --    |
|  ![buttonTelegram](https://i.imgur.com/j2np8rg.jpg)  |  ![buttonTelegram](https://i.imgur.com/lWp1bKw.jpg)  |

#### I remind you to change the entities of your devices in the code (climate, temperature sensors, switches ...)

## Versione 2.0
In this second version I added two operating modes:

![Lovelace](https://i.imgur.com/FcgOm4I.jpg)

- AWAY Mode (I am away from home and the reference temperature is set at 17° C, therefore as if it were manual, but with a different setPoint temperature. This temperature can be changed in the automation code)
- TurnOFF (I turn everything off, from climate to automation)

The package has been updated as well as the part of the telegram buttons and finally the lovelace part.

In detail.
An _input_boolean.away_mode_ has been added, which defines or not the away mode
In the first version, a history_stats sensor was introduced, referring to the period of heating of the radiators in the last 24 hours, namely _yesterday_.
Thus, from this sensor, the template was created, readable on a human level indicating _hh:mm:ss_.

With the update, another history_stats sensor has been added for a personal need.
This time the count is from midnight of the current day until the moment I request this value, _00:00-now_, so to speak!
This also has its own template below, for a human level.

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

