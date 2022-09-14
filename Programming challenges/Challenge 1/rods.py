rods = float(input('Enter your distance in rods'))
meters = rods * 5.0292
print(meters)
furlong = rods / 40
print(furlong)
mile = meters / 1609.34
print(mile)
foot = meters / 0.3048
AWS = mile / 3.1
print('It will take '+str(AWS)+' hours to travel your distance')

def meters(rods):
    return rods * 5.0292

def furlong(rods):
    return rods / 40

def mile(meters):
    return meters / 1609.34

def foot(meters):
    return meters / 0.3048

def AWS(mile):
    time = mile / 3.1
    return('It will take '+str(time)+' hours to travel your distance')





    
