def find_temp(air_temp,air_speed):
    windchill = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return (f'Temperature of {air_temp} and speed of {air_speed} gives windchill of: {windchill}')

print(find_temp(10,15))
print(find_temp(0,25))
print(find_temp(-10,35))

Temp = float(input('Enter an air temperature: '))
Speed = float(input('Enter an air speed: '))

def find_chill(air_temp,air_speed):
    WINDCHILL = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return(WINDCHILL)

print(f'Windchill: {find_chill(Temp,Speed)}')

    
    


           
