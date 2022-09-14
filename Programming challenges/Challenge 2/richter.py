richter = float(input('Enter a Richter Scale measurement: '))
energy = 10**1.5*richter+4.8
TNT = energy / 4.184*10**9
print('Richter value: '+str(richter))
print('Equivalence in joules: '+str(energy))
print('Equivalence in tons of TNT: '+str(TNT))



