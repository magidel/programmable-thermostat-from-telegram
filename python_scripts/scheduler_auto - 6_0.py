""" Scheduler V2 by MaGiDeL for HassioHelp 
    For Question ask in forum.hassiohelp.eu or in Group Telegram """

###########################################################################################################
### FUNCTIONS
###########################################################################################################
def strptime(time_str):
    parts = str(time_str).split(':')
    if len(parts) < 1:
        return
    try:
        hour = int(parts[0])
        minute = int(parts[1])
        return datetime.time(hour, minute)
    except ValueError:
        # ValueError if value cannot be converted to an int or not in range
        return None

def isTimeFormat(timevar):
    if len(timevar)==5 and timevar[:2].isdigit() and timevar[2]==':' and timevar[3:].isdigit():
        return True
    else:
        return False

def isTempFormat(tempvar):
    if len(tempvar)==4 and tempvar[:2].isdigit() and tempvar[2]=='.' and tempvar[3].isdigit():
        return True
    else:
        return False

def schedule(switch,on,off,zone,temp):
    a=[]
    if switch=='off':
        return a
    else:
        for item2,item3,item4,item5 in zip(on,off,zone,temp):
            if isTimeFormat(item2) and isTimeFormat(item3) and isTempFormat(item5):
                t1=strptime(item2)
                t2=strptime(item3)
                b=[t1,t2,item4,item5]
                a.append(b)
    return a

###########################################################################################################
### SCHEDULER VAR
###########################################################################################################
####### Monday
LUN_SWITCH_THERMO = hass.states.get('input_boolean.lun_switch_thermo').state
LUN_ON_THERMO = [hass.states.get('input_text.lun_1_on_thermo').state,hass.states.get('input_text.lun_2_on_thermo').state,hass.states.get('input_text.lun_3_on_thermo').state,hass.states.get('input_text.lun_4_on_thermo').state,hass.states.get('input_text.lun_5_on_thermo').state]
LUN_OFF_THERMO = [hass.states.get('input_text.lun_1_off_thermo').state,hass.states.get('input_text.lun_2_off_thermo').state,hass.states.get('input_text.lun_3_off_thermo').state,hass.states.get('input_text.lun_4_off_thermo').state,hass.states.get('input_text.lun_5_off_thermo').state]
LUN_THERMAL_ZONE = [hass.states.get('input_select.lun_1_zone').state,hass.states.get('input_select.lun_2_zone').state,hass.states.get('input_select.lun_3_zone').state,hass.states.get('input_select.lun_4_zone').state,hass.states.get('input_select.lun_5_zone').state]
LUN_THERMAL_TEMP = [hass.states.get('input_text.lun_1_temp').state,hass.states.get('input_text.lun_2_temp').state,hass.states.get('input_text.lun_3_temp').state,hass.states.get('input_text.lun_4_temp').state,hass.states.get('input_text.lun_5_temp').state]
LUN_SCHEDULE_THERMO = schedule(LUN_SWITCH_THERMO, LUN_ON_THERMO, LUN_OFF_THERMO, LUN_THERMAL_ZONE, LUN_THERMAL_TEMP)

####### Tuesday
MAR_SWITCH_THERMO = hass.states.get('input_boolean.mar_switch_thermo').state
MAR_ON_THERMO = [hass.states.get('input_text.mar_1_on_thermo').state,hass.states.get('input_text.mar_2_on_thermo').state,hass.states.get('input_text.mar_3_on_thermo').state,hass.states.get('input_text.mar_4_on_thermo').state,hass.states.get('input_text.mar_5_on_thermo').state]
MAR_OFF_THERMO = [hass.states.get('input_text.mar_1_off_thermo').state,hass.states.get('input_text.mar_2_off_thermo').state,hass.states.get('input_text.mar_3_off_thermo').state,hass.states.get('input_text.mar_4_off_thermo').state,hass.states.get('input_text.mar_5_off_thermo').state]
MAR_THERMAL_ZONE = [hass.states.get('input_select.mar_1_zone').state,hass.states.get('input_select.mar_2_zone').state,hass.states.get('input_select.mar_3_zone').state,hass.states.get('input_select.mar_4_zone').state,hass.states.get('input_select.mar_5_zone').state]
MAR_THERMAL_TEMP = [hass.states.get('input_text.mar_1_temp').state,hass.states.get('input_text.mar_2_temp').state,hass.states.get('input_text.mar_3_temp').state,hass.states.get('input_text.mar_4_temp').state,hass.states.get('input_text.mar_5_temp').state]
MAR_SCHEDULE_THERMO = schedule(MAR_SWITCH_THERMO, MAR_ON_THERMO, MAR_OFF_THERMO, MAR_THERMAL_ZONE, MAR_THERMAL_TEMP)

####### Wednesday
MER_SWITCH_THERMO = hass.states.get('input_boolean.mer_switch_thermo').state
MER_ON_THERMO = [hass.states.get('input_text.mer_1_on_thermo').state,hass.states.get('input_text.mer_2_on_thermo').state,hass.states.get('input_text.mer_3_on_thermo').state,hass.states.get('input_text.mer_4_on_thermo').state,hass.states.get('input_text.mer_5_on_thermo').state]
MER_OFF_THERMO = [hass.states.get('input_text.mer_1_off_thermo').state,hass.states.get('input_text.mer_2_off_thermo').state,hass.states.get('input_text.mer_3_off_thermo').state,hass.states.get('input_text.mer_4_off_thermo').state,hass.states.get('input_text.mer_5_off_thermo').state]
MER_THERMAL_ZONE = [hass.states.get('input_select.mer_1_zone').state,hass.states.get('input_select.mer_2_zone').state,hass.states.get('input_select.mer_3_zone').state,hass.states.get('input_select.mer_4_zone').state,hass.states.get('input_select.mer_5_zone').state]
MER_THERMAL_TEMP = [hass.states.get('input_text.mer_1_temp').state,hass.states.get('input_text.mer_2_temp').state,hass.states.get('input_text.mer_3_temp').state,hass.states.get('input_text.mer_4_temp').state,hass.states.get('input_text.mer_5_temp').state]
MER_SCHEDULE_THERMO = schedule(MER_SWITCH_THERMO, MER_ON_THERMO, MER_OFF_THERMO, MER_THERMAL_ZONE, MER_THERMAL_TEMP)

####### Thursday
GIO_SWITCH_THERMO = hass.states.get('input_boolean.gio_switch_thermo').state
GIO_ON_THERMO = [hass.states.get('input_text.gio_1_on_thermo').state,hass.states.get('input_text.gio_2_on_thermo').state,hass.states.get('input_text.gio_3_on_thermo').state,hass.states.get('input_text.gio_4_on_thermo').state,hass.states.get('input_text.gio_5_on_thermo').state]
GIO_OFF_THERMO = [hass.states.get('input_text.gio_1_off_thermo').state,hass.states.get('input_text.gio_2_off_thermo').state,hass.states.get('input_text.gio_3_off_thermo').state,hass.states.get('input_text.gio_4_off_thermo').state,hass.states.get('input_text.gio_5_off_thermo').state]
GIO_THERMAL_ZONE = [hass.states.get('input_select.gio_1_zone').state,hass.states.get('input_select.gio_2_zone').state,hass.states.get('input_select.gio_3_zone').state,hass.states.get('input_select.gio_4_zone').state,hass.states.get('input_select.gio_5_zone').state]
GIO_THERMAL_TEMP = [hass.states.get('input_text.gio_1_temp').state,hass.states.get('input_text.gio_2_temp').state,hass.states.get('input_text.gio_3_temp').state,hass.states.get('input_text.gio_4_temp').state,hass.states.get('input_text.gio_5_temp').state]
GIO_SCHEDULE_THERMO = schedule(GIO_SWITCH_THERMO, GIO_ON_THERMO, GIO_OFF_THERMO, GIO_THERMAL_ZONE, GIO_THERMAL_TEMP)

####### Friday
VEN_SWITCH_THERMO = hass.states.get('input_boolean.ven_switch_thermo').state
VEN_ON_THERMO = [hass.states.get('input_text.ven_1_on_thermo').state,hass.states.get('input_text.ven_2_on_thermo').state,hass.states.get('input_text.ven_3_on_thermo').state,hass.states.get('input_text.ven_4_on_thermo').state,hass.states.get('input_text.ven_5_on_thermo').state]
VEN_OFF_THERMO = [hass.states.get('input_text.ven_1_off_thermo').state,hass.states.get('input_text.ven_2_off_thermo').state,hass.states.get('input_text.ven_3_off_thermo').state,hass.states.get('input_text.ven_4_off_thermo').state,hass.states.get('input_text.ven_5_off_thermo').state]
VEN_THERMAL_ZONE = [hass.states.get('input_select.ven_1_zone').state,hass.states.get('input_select.ven_2_zone').state,hass.states.get('input_select.ven_3_zone').state,hass.states.get('input_select.ven_4_zone').state,hass.states.get('input_select.ven_5_zone').state]
VEN_THERMAL_TEMP = [hass.states.get('input_text.ven_1_temp').state,hass.states.get('input_text.ven_2_temp').state,hass.states.get('input_text.ven_3_temp').state,hass.states.get('input_text.ven_4_temp').state,hass.states.get('input_text.ven_5_temp').state]
VEN_SCHEDULE_THERMO = schedule(VEN_SWITCH_THERMO, VEN_ON_THERMO, VEN_OFF_THERMO, VEN_THERMAL_ZONE, VEN_THERMAL_TEMP)

####### Saturday
SAB_SWITCH_THERMO = hass.states.get('input_boolean.sab_switch_thermo').state
SAB_ON_THERMO = [hass.states.get('input_text.sab_1_on_thermo').state,hass.states.get('input_text.sab_2_on_thermo').state,hass.states.get('input_text.sab_3_on_thermo').state,hass.states.get('input_text.sab_4_on_thermo').state,hass.states.get('input_text.sab_5_on_thermo').state]
SAB_OFF_THERMO = [hass.states.get('input_text.sab_1_off_thermo').state,hass.states.get('input_text.sab_2_off_thermo').state,hass.states.get('input_text.sab_3_off_thermo').state,hass.states.get('input_text.sab_4_off_thermo').state,hass.states.get('input_text.sab_5_off_thermo').state]
SAB_THERMAL_ZONE = [hass.states.get('input_select.sab_1_zone').state,hass.states.get('input_select.sab_2_zone').state,hass.states.get('input_select.sab_3_zone').state,hass.states.get('input_select.sab_4_zone').state,hass.states.get('input_select.sab_5_zone').state]
SAB_THERMAL_TEMP = [hass.states.get('input_text.sab_1_temp').state,hass.states.get('input_text.sab_2_temp').state,hass.states.get('input_text.sab_3_temp').state,hass.states.get('input_text.sab_4_temp').state,hass.states.get('input_text.sab_5_temp').state]
SAB_SCHEDULE_THERMO = schedule(SAB_SWITCH_THERMO, SAB_ON_THERMO, SAB_OFF_THERMO, SAB_THERMAL_ZONE, SAB_THERMAL_TEMP)

####### Sunday
DOM_SWITCH_THERMO = hass.states.get('input_boolean.dom_switch_thermo').state
DOM_ON_THERMO = [hass.states.get('input_text.dom_1_on_thermo').state,hass.states.get('input_text.dom_2_on_thermo').state,hass.states.get('input_text.dom_3_on_thermo').state,hass.states.get('input_text.dom_4_on_thermo').state,hass.states.get('input_text.dom_5_on_thermo').state]
DOM_OFF_THERMO = [hass.states.get('input_text.dom_1_off_thermo').state,hass.states.get('input_text.dom_2_off_thermo').state,hass.states.get('input_text.dom_3_off_thermo').state,hass.states.get('input_text.dom_4_off_thermo').state,hass.states.get('input_text.dom_5_off_thermo').state]
DOM_THERMAL_ZONE = [hass.states.get('input_select.dom_1_zone').state,hass.states.get('input_select.dom_2_zone').state,hass.states.get('input_select.dom_3_zone').state,hass.states.get('input_select.dom_4_zone').state,hass.states.get('input_select.dom_5_zone').state]
DOM_THERMAL_TEMP = [hass.states.get('input_text.dom_1_temp').state,hass.states.get('input_text.dom_2_temp').state,hass.states.get('input_text.dom_3_temp').state,hass.states.get('input_text.dom_4_temp').state,hass.states.get('input_text.dom_5_temp').state]
DOM_SCHEDULE_THERMO = schedule(DOM_SWITCH_THERMO, DOM_ON_THERMO, DOM_OFF_THERMO, DOM_THERMAL_ZONE, DOM_THERMAL_TEMP)


###########################################################################################################
### CLIMATIC VAR
###########################################################################################################
LOW_SETPOINT = hass.states.get('input_number.low_setpoint')
climate_entity = 'climate.generic_thermo'
# current_temp = hass.states.get(climate_entity).attributes['current_temperature']


###########################################################################################################
### IF SECTIONS
###########################################################################################################

if datetime.datetime.now().date().weekday() == 0:
    current_schedule = LUN_SCHEDULE_THERMO
elif datetime.datetime.now().date().weekday() == 1:
    current_schedule = MAR_SCHEDULE_THERMO
elif datetime.datetime.now().date().weekday() == 2:
    current_schedule = MER_SCHEDULE_THERMO
elif datetime.datetime.now().date().weekday() == 3:
    current_schedule = GIO_SCHEDULE_THERMO
elif datetime.datetime.now().date().weekday() == 4:
    current_schedule = VEN_SCHEDULE_THERMO
elif datetime.datetime.now().date().weekday() == 5:
    current_schedule = SAB_SCHEDULE_THERMO
else:
    current_schedule = DOM_SCHEDULE_THERMO

#-----------------
# logger.info("current_schedule: %s", current_schedule)
#-----------------


now = datetime.datetime.now().time()
in_high_time = False
for high_time in current_schedule:
    start = high_time[0]
    end = high_time[1]
    current_zone = high_time[2]
    current_setpoint = high_time[3]
    if start <= now <= end:
        in_high_time = True
        break


if current_zone == 'Beds':
    current_temp = hass.states.get('sensor.avgtempbed').state
elif current_zone == 'Living':
    current_temp = hass.states.get('sensor.avgtempliving').state
elif current_zone == 'All':
    current_temp = hass.states.get('sensor.avgtempall').state
else:
    logger.info("current_zone not find")

#-----------------
# logger.info("now: %s", now)
# logger.info("in_high_time: %s", in_high_time)
# logger.info("current_zone: %s", current_zone)
# logger.info("current_temp: %s", current_temp)
# logger.info("current_setpoint: %s", current_setpoint)
#-----------------


###########################################################################################################
### ASSIGNMENT
###########################################################################################################

new_setpoint = current_setpoint if in_high_time else LOW_SETPOINT
hass.states.set('sensor.current_zone', current_zone)
hass.states.set('sensor.current_temp', current_temp)
hass.states.set('sensor.current_setpoint', current_setpoint)


#-----------------
# logger.info("new_setpoint: %s", new_setpoint)
#-----------------

if str(new_setpoint) != str(current_temp):
    hass.services.call( 'climate', 'set_temperature', { 'entity_id': climate_entity, 'temperature': float(new_setpoint) } )