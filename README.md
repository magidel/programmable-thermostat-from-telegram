![Version](https://img.shields.io/badge/Version-6.5-green)
[![Platform](https://img.shields.io/badge/Platform-Hassio-yellow)](https://www.home-assistant.io/hassio/installation/)
[![hassiohelp](https://img.shields.io/badge/Forum-hassiohelp-blue)](https://hassiohelp.eu/2019/12/21/termostato-programmabile/)

[![Telegram](https://img.shields.io/badge/Need-buttonTelegram-red)](https://hassiohelp.eu/2019/03/17/bot-telegram/)
![notNeed](https://img.shields.io/badge/notNeed-GoogleHome,Alexa-lightgrey)
![notNeed](https://img.shields.io/badge/notNeed-deviceTracker-lightgrey)

# Programmable thermostat from Telegram

## Version 6.5

![Lovelace](https://i.imgur.com/IthVz9q.jpg)

   #### New video: https://www.youtube.com/watch?v=KuQIP6OYA7g

Italian Support: HassioHelp
 
   Telegram https://t.me/HassioHelp
   
   Facebook https://www.facebook.com/groups/2062381507393179
   
   WebSite https://hassiohelp.eu/2019/12/21/termostato-programmabile/
   
   Forum https://forum.hassiohelp.eu/d/515-termostato-programmabile-da-telegram

- #### Added enhancement for viewing on tablet
  The UI for viewing on tablets has been improved. The various buttons activate and deactivate the view of the columns for programming.

- #### Added highlight on current event
  Both the current day and time period are now highlighted

- #### Fixed an minor error on the python file about LowSetpoint

- #### Telegram part has not changed. Version 6.0 can be used.

## Version 6.0

![Lovelace](https://i.imgur.com/IMMpP78.jpg)

   video: https://youtu.be/yEF4qnM_ENA

After creating the zones, why not consider the reference temperatures for each zone?
From here we started for the umpteenth update of the package.

The operation of the thermostat was based on three variables:
- boiler ignition time
- shutdown time
- reference zone, so as to be able to choose the target of the zone
A fourth has been added to these three variables: the reference temperature.
In this way, it is thought to be able to manage the thermostat in all its parts and for every subjective need.

Some "trappings" used up to version 5.0 have been removed, making the code more streamlined.
The boost mode has been eliminated. Now you don't need it anymore, just set the temperature in the desired period.
The code of the telegram part has been revised, completely cleaned of unnecessary references, recalls and redundant parts and updated to the new sensors.
The HIGH temperatures, one of the two reference temperatures together with the LOW, has been transformed into the setpoint temperature that is set at each period.
the LOW remained unchanged.
Rearrange the three modes AUTO, MANUAL and AWAY so that they all have the same behavior.
AWAY mode is a MANUAL mode with fixed zone and setpoint.

Disruption of the GUI.
Calendar mode has been dropped.
Both the picture-entity and the multi-row card have been replaced by a grid of button cards, with the full range of settings that this card makes available.
The number of periods that can be used have been increased to 5, to increase the number of combinations during the day.
Nothing prevents you from adding other periods as needed.
Each line refers to the day of the week.
In the column "dey week" the buttons activate and deactivate the programming for the whole day, keeping track of the current day for a better view.
Each variable referred to the period (switch-on time, switch-off time, thermal zone, reference temperature) is activated when it is set. If left without value it is disabled.

If you have any suggestions for the graphical interface, do not hesitate to contact me ... I am always available to find better solutions! ;)


## Version 5.0

![Lovelace](https://i.imgur.com/9Xx6L0V.jpg)

- #### Added Zone programming and new GUI for weekly program
  The development of the package has always been linked to family needs which can vary.
  Specifically, the change of house involves different climatic characteristics than the previous one.
  The "target_sensor" of the "climate" entity had to be managed no longer as before, single and fixed (the average between two well-defined temperatures), but by zone (for example day and night) precisely due to the characteristics of the new apartment.
  Not having thermostatic heads available to the radiators (see also the cost for each valve), it was decided to use only the temperature sensors to create thermal zones.
  This new packege introduces the choice of the area, among the many defined a priori.
  Each zone is associated with an average temperature (for example the BedRooms zone will have the average temperature of the two bedrooms as "target_sensor"). By choosing that zone, the boiler will work only for that zone, that is, it will heat up until the current temperature (the "target_sensor, or the temperature of the selected zone) does not equal the reference temperature (for example set at 20 ° C).
  In using this way of operating, in other areas, most likely, the average temperature will go above or below the "target_sensor" of the "climate" entity (for example, since the rooms are colder in the living area, this the latter will be heated more, above the set reference temperature). The temperature differences between the zones set, however, are around the single degree, so this zone approximation is welcome.

Going into detail, we wanted to leave all the functions introduced in previous versions, including AUTO and MANUAL mode.

If you prefer one or the other, you have the opportunity to set the reference zone.

In the case of MANUAL mode, the only parameters are the thermal zone and the reference temperature. The picture below as an example:

![Manual](https://i.imgur.com/kKUBi0Y.jpg)

In the case of AUTO mode, the choice of the zone is linked to the time slot of interest.

The package has been designed to manage up to 4 time intervals, in which the start-up and shutdown times of the boiler are set.

The setting of the thermal zone has also been added to these times, so as to concentrate the heat in the area and time slot concerned.

![Auto](https://i.imgur.com/pgM69Ga.jpg)

By introducing the concept of zones, the choice of the thermal zone was added in the previous YAML interface, following the time band.

For a better view, a "picture-elements" card has been introduced which represents the entire week with the various time bands and the related thermal zones.

With an input_boolean ("Calendar mode", see the picture below) you can choose between the two lovelace cards.

![Calendar](https://i.imgur.com/pjF0DvC.jpg)


Finally, for completeness, the avgtemp sensors (average temperatures of the zones) and the thermohygrometric index were inserted directly into the package.

For the colors of the thermohygrometric index I added a theme to insert in the themes folder.
  ```yaml
  themes: !include_dir_merge_named themes/
  ```

#### Images from telegram
| main screen | AUTO mode | MANUAL mode |
|    --    |    --    |    --    |
|  ![main](https://i.imgur.com/lp1sxyR.jpg)  |  ![auto](https://i.imgur.com/bjHGgMo.jpg)  |  ![manual](https://i.imgur.com/DMupSUc.jpg)  |


## Version 4.0

![Lovelace](https://i.imgur.com/2UvhqgI.jpg)

- #### Necessary requirement:
  card: Multiple Entity Row (https://github.com/benct/lovelace-multiple-entity-row)

- #### Added the GUI for weekly programming
  Given the forced stay in the home, the UI is increasingly used compared to simple telegram messages / buttons.
  This has led to even more attention to the appearance of the thermostat package.
  In fact, there was no "visual" programming, a scheduler that can be edited directly from the UI, without putting your hand to the .py file.
  It was therefore decided to put on a scheduler for the weekly programming of the boiler.
  The daily programming has been set in 4 states (ON and OFF for each state), therefore in total 8 states, for each day of the week.
  So you can turn it on and off 4 times a day.
  It was decided to use input_text instead of input_datetime to be able to insert any wording (any text, for example "null") that "cancels" the time in that state.
  Not only is there a pattern to follow in the input_text declaration, but in the .py file there is a control over the text coming from the UI.
  In addition, an input_boolean called switch has been added for each day, which defines the activation or deactivation in the day's programming.
  The input_boolean variable to confirm the presence or absence during the weekend at home has now been "hooked" to the switches described above on Saturday and Sunday.
  
A note to the .py file.
Unfortunately the function "datetime.strptime ()" present and very useful in python, in the python instance launched in Hassio it is not present, it is not even possible to import it.
So rewrote this function to traform input_text into real time variables.
The schedule () function, on the other hand, creates the "current_schedule" based on information from the UI.
The rest of the script does not vary in substance from the previous version. 

- #### Conclusion and future developments 
  The scheduler defined before in the .py file, now, instead, derives directly from the UI.
  
  But why stop at the boiler program?
  If you notice the python script better, the "climate.set_temperature" service is called. Indeed:
  ```python
  hass.services.call ('climate', 'set_temperature', ...
  ```
  So you could think of using another service, for example "remote.turn_on", so as to use the Broadlink to program the ignition of anything (air conditioner, robot ...).
  
The limit as always depends on all of us!

Final result:
![Lovelace](https://i.imgur.com/Zbt2Zgc.jpg)


## Version 3.6

- #### Added two automations when Hassio restart useful for the memory of the climate system.
  Under the conditions if the AUTO mode is ON then the AUTO automation is activated.
  In a dual way, the condition of the second automation concerns the MANUAL mode.

Also corrected the MANUAL automation setting action, using the template of the variable "input_number.setpoint".

## Version 3.5
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



## Version 3.0
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

## Version 2.0
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

First of all, this is the only hardware component used, the best for this purpose:

[Shelly 1](https://shelly.cloud/shelly1-open-source/)

therefore for use with the boiler, the clean contact (potential free relay contact) was used that the shelly offers us:
![shelly](https://i.imgur.com/csJOK2E.jpg)

Wire connections description scheme from shelly to boiler:
![sheme](https://i.imgur.com/FFQCscr.png)

The phsycal button is used to start the boiler manually, without going through any program hassio!

This is the app configuration:

![app](https://i.imgur.com/iA5n0RD.jpg)

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

