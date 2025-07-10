

from numpy import random
import time

# ACTUATOR STATUS
def actuator_status():
    actuator = random.choice(["off", "on"])
    return f"Actuator = {actuator}"

# TEMPERATURE STATUS
def temp_status():
    sensor_temp = round(random.uniform(-15, 120), 2)
    if sensor_temp < 20:
        return f"Low temperature alert!\nTemperature = {sensor_temp} °C"
    elif sensor_temp > 105:
        return f"High temperature alert!\nTemperature = {sensor_temp} °C"
    else:
        return f"Temperature = {sensor_temp} °C"

# PRESSURE STATUS
def pressure_status():
    sensor_pressure = random.randint(0, 1000)
    if sensor_pressure < 250:
        return f"Low pressure alert!\nPressure = {sensor_pressure} Pa"
    elif sensor_pressure > 750:
        return f"High pressure alert!\nPressure = {sensor_pressure} Pa"
    else:
        return f"Pressure = {sensor_pressure} Pa"

# VOLTAGE STATUS
def volt_status():
    sensor_voltage = random.randint(0, 50000)
    if sensor_voltage < 1000:
        return f"Low voltage alert!\nVoltage = {sensor_voltage} V"
    elif sensor_voltage > 40000:
        return f"High voltage alert!\nVoltage = {sensor_voltage} V"
    else:
        return f"Voltage = {sensor_voltage} V"

# TIMESTAMP FUNCTION WITH LOGGING
def timestamp(actuator_status, temp_status, pressure_status, volt_status, log_file='system_log.txt'):
    # Prepare the log entry
    log_entry = '[{}] System Status Report:\n'.format(time.strftime("%Y-%m-%d %H:%M:%S"))
    log_entry += f"{actuator_status}\n"
    log_entry += f"{temp_status}\n"
    log_entry += f"{pressure_status}\n"
    log_entry += f"{volt_status}\n"
    log_entry += "-" * 50 + "\n"  # To separate each entry
    
    # Open log file and append the log entry
    with open(log_file, 'a') as file:
        file.write(log_entry)

    # Optionally, print it out to the console as well
    print(log_entry)

# Call and pass values
timestamp(
    actuator_status, temp_status, pressure_status, volt_status
)
