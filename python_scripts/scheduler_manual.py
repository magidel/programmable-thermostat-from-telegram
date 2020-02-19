SETPOINT = 'input_number.setpoint'
climate_entity = 'climate.generic_thermo'
current_temp = hass.states.get(climate_entity).attributes['current_temperature']

if current_temp < SETPOINT:
    hass.services.call( 'climate', 'set_temperature', { 'entity_id': climate_entity, 'temperature': SETPOINT } )
