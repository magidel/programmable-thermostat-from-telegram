TEMP_HIGH = hass.states.get('input_number.temp_high')
TEMP_LOW = hass.states.get('input_number.temp_low')
WEEKEND_ON = hass.states.get('input_boolean.weekend_on')
climate_entity = 'climate.generic_thermo'
current_temp = hass.states.get(climate_entity).attributes['current_temperature']

WEEK_SCHEDULE = [
    [datetime.time( 0, 0), datetime.time( 7, 30)],      # dalle 00:00 alle 07:30
    [datetime.time(12, 30), datetime.time(23, 59, 59)]   # dalle 12:30 alle 23:59
]
WEEKEND_OFF_SCHEDULE = [
]
WEEKEND_ON_SCHEDULE = [
    [datetime.time( 0, 0), datetime.time( 23, 59,59)],     # dalle 00:00 alle 23:59
]

now = datetime.datetime.now().time()
if datetime.datetime.now().date().weekday() < 5:
    current_schedule = WEEK_SCHEDULE
elif WEEKEND_ON.state == 'on':
    current_schedule = WEEKEND_ON_SCHEDULE
else:
    current_schedule = WEEKEND_OFF_SCHEDULE

in_high_time = False
for high_time in current_schedule:
    start = high_time[0]
    end = high_time[1]
    if start <= now <= end:
        in_high_time = True
        break

new_temp = TEMP_HIGH if in_high_time else TEMP_LOW 
if str(new_temp.state) != str(current_temp):
    hass.services.call( 'climate', 'set_temperature', { 'entity_id': climate_entity, 'temperature': float(new_temp.state) } )



