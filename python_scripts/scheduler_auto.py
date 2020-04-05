""" Scheduler V1 by MaGiDeL for HassioHelp 
    For Question ask in forum.hassiohelp.eu or in Group Telegram """

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

def isTimeFormat(input1):
    if len(input1)==5 and input1[:2].isdigit() and input1[2]==':' and input1[3:].isdigit():
        return True
    else:
        return False

def schedule(input1,input2,input3):
    a=[]
    if input1=='off':
        return a
    else:
        for item2,item3 in zip(input2,input3):
            if isTimeFormat(item2) and isTimeFormat(item3):
                t1=strptime(item2)
                t2=strptime(item3)
                b=[t1,t2]
                a.append(b)
    return a

###################### scheduler variables ######################
####### LUNEDI
LUN_SWITCH = hass.states.get('input_boolean.lun_switch').state
LUN_ON = [hass.states.get('input_text.lun_1_on').state,hass.states.get('input_text.lun_2_on').state,hass.states.get('input_text.lun_3_on').state,hass.states.get('input_text.lun_4_on').state]
LUN_OFF = [hass.states.get('input_text.lun_1_off').state,hass.states.get('input_text.lun_2_off').state,hass.states.get('input_text.lun_3_off').state,hass.states.get('input_text.lun_4_off').state]
LUN_SCHEDULE = schedule(LUN_SWITCH, LUN_ON, LUN_OFF)

# logger.info("LUN_SCHEDULE: %s", LUN_SCHEDULE)

####### MARTEDI
MAR_SWITCH = hass.states.get('input_boolean.mar_switch').state
MAR_ON = [hass.states.get('input_text.mar_1_on').state,hass.states.get('input_text.mar_2_on').state,hass.states.get('input_text.mar_3_on').state,hass.states.get('input_text.mar_4_on').state]
MAR_OFF = [hass.states.get('input_text.mar_1_off').state,hass.states.get('input_text.mar_2_off').state,hass.states.get('input_text.mar_3_off').state,hass.states.get('input_text.mar_4_off').state]
MAR_SCHEDULE = schedule(MAR_SWITCH, MAR_ON, MAR_OFF)

# logger.info("MAR_SCHEDULE: %s", MAR_SCHEDULE)

####### MERCOLEDI
MER_SWITCH = hass.states.get('input_boolean.mer_switch').state
MER_ON = [hass.states.get('input_text.mer_1_on').state,hass.states.get('input_text.mer_2_on').state,hass.states.get('input_text.mer_3_on').state,hass.states.get('input_text.mer_4_on').state]
MER_OFF = [hass.states.get('input_text.mer_1_off').state,hass.states.get('input_text.mer_2_off').state,hass.states.get('input_text.mer_3_off').state,hass.states.get('input_text.mer_4_off').state]
MER_SCHEDULE = schedule(MER_SWITCH, MER_ON, MER_OFF)

# logger.info("MER_SCHEDULE: %s", MER_SCHEDULE)

####### GIOVEDI
GIO_SWITCH = hass.states.get('input_boolean.gio_switch').state
GIO_ON = [hass.states.get('input_text.gio_1_on').state,hass.states.get('input_text.gio_2_on').state,hass.states.get('input_text.gio_3_on').state,hass.states.get('input_text.gio_4_on').state]
GIO_OFF = [hass.states.get('input_text.gio_1_off').state,hass.states.get('input_text.gio_2_off').state,hass.states.get('input_text.gio_3_off').state,hass.states.get('input_text.gio_4_off').state]
GIO_SCHEDULE = schedule(GIO_SWITCH, GIO_ON, GIO_OFF)

# logger.info("GIO_SCHEDULE: %s", GIO_SCHEDULE)

####### VENERDI
VEN_SWITCH = hass.states.get('input_boolean.ven_switch').state
VEN_ON = [hass.states.get('input_text.ven_1_on').state,hass.states.get('input_text.ven_2_on').state,hass.states.get('input_text.ven_3_on').state,hass.states.get('input_text.ven_4_on').state]
VEN_OFF = [hass.states.get('input_text.ven_1_off').state,hass.states.get('input_text.ven_2_off').state,hass.states.get('input_text.ven_3_off').state,hass.states.get('input_text.ven_4_off').state]
VEN_SCHEDULE = schedule(VEN_SWITCH, VEN_ON, VEN_OFF)

# logger.info("VEN_SCHEDULE: %s", VEN_SCHEDULE)

####### SABATO
SAB_SWITCH = hass.states.get('input_boolean.sab_switch').state
SAB_ON = [hass.states.get('input_text.sab_1_on').state,hass.states.get('input_text.sab_2_on').state,hass.states.get('input_text.sab_3_on').state,hass.states.get('input_text.sab_4_on').state]
SAB_OFF = [hass.states.get('input_text.sab_1_off').state,hass.states.get('input_text.sab_2_off').state,hass.states.get('input_text.sab_3_off').state,hass.states.get('input_text.sab_4_off').state]
SAB_SCHEDULE = schedule(SAB_SWITCH, SAB_ON, SAB_OFF)

# logger.info("SAB_SCHEDULE: %s", SAB_SCHEDULE)
# logger.info("SAB_ON: %s", SAB_ON)
# logger.info("SAB_OFF: %s", SAB_OFF)

####### DOMENICA
DOM_SWITCH = hass.states.get('input_boolean.dom_switch').state
DOM_ON = [hass.states.get('input_text.dom_1_on').state,hass.states.get('input_text.dom_2_on').state,hass.states.get('input_text.dom_3_on').state,hass.states.get('input_text.dom_4_on').state]
DOM_OFF = [hass.states.get('input_text.dom_1_off').state,hass.states.get('input_text.dom_2_off').state,hass.states.get('input_text.dom_3_off').state,hass.states.get('input_text.dom_4_off').state]
DOM_SCHEDULE = schedule(DOM_SWITCH, DOM_ON, DOM_OFF)

# logger.info("DOM_SCHEDULE: %s", DOM_SCHEDULE)
# logger.info("DOM_ON: %s", DOM_ON)
# logger.info("DOM_OFF: %s", DOM_OFF)


###################### climatic variables ######################
TEMP_HIGH = hass.states.get('input_number.temp_high')
TEMP_LOW = hass.states.get('input_number.temp_low')
#WEEKEND_ON = hass.states.get('input_boolean.weekend_on').state
climate_entity = 'climate.generic_thermo'
current_temp = hass.states.get(climate_entity).attributes['current_temperature']

if datetime.datetime.now().date().weekday() == 0:
    current_schedule = LUN_SCHEDULE
elif datetime.datetime.now().date().weekday() == 1:
    current_schedule = MAR_SCHEDULE
elif datetime.datetime.now().date().weekday() == 2:
    current_schedule = MER_SCHEDULE
elif datetime.datetime.now().date().weekday() == 3:
    current_schedule = GIO_SCHEDULE
elif datetime.datetime.now().date().weekday() == 4:
    current_schedule = VEN_SCHEDULE
elif datetime.datetime.now().date().weekday() == 5:
    current_schedule = SAB_SCHEDULE
else:
    current_schedule = DOM_SCHEDULE

logger.info("current_schedule: %s", current_schedule)

now = datetime.datetime.now().time()

in_high_time = False
for high_time in current_schedule:
    start = high_time[0]
    end = high_time[1]
    if start <= now <= end:
        in_high_time = True
        break

logger.info("now: %s", now)
logger.info("in_high_time: %s", in_high_time)
if in_high_time:
    message = "TEMP_HIGH"
    hass.services.call('notify', 'telegram', {'title' : '*Test*', 'message': message})
else:
    message = "TEMP_LOW"
    hass.services.call('notify', 'telegram', {'title' : '*Test*', 'message': message})

logger.info("message: %s", message)


new_temp = TEMP_HIGH if in_high_time else TEMP_LOW 

# message = "Set Temperature at: {} (old temp: {}) from scheduler".format(new_temp.state, current_temp)
if str(new_temp.state) != str(current_temp):
    # imposta la nuova temperatura sul termostato
    hass.services.call( 'climate', 'set_temperature', { 'entity_id': climate_entity, 'temperature': float(new_temp.state) } )