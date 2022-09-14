

def meters(Rods):
    return Rods * 5.0292

def furlong(ROds):
    return ROds / 40

def mile(meters):
    return meters / 1609.34

def foot(meters):
    return meters / 0.3048

def AWS(mile):
    time = mile / 3.1
    return('It will take '+str(time)+' hours to travel your distance')

rods = float(input('Enter your distance in rods'))
print('Your distance is equal to '+str(meters(rods)) +' metres' )
print('Your distance is equal to '+ str(furlong(rods))+' furlongs')
Metres = meters(rods)
print('Your distance is equal to '+str(mile(Metres))+' miles')
print('Your distance is equal to '+str(foot(Metres))+' feet')
Miles = mile(Metres)
x = AWS(Miles)
print(x)



    
