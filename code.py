
import math
import time
import datetime
# Will print the accelerometer & magnetometer X, Y, Z axis values every half second instead of 1/8
.
import Adafruit_LSM303
# Import the LSM303(accelerometer) module. 

#makes LSM303 
lsm303 = Adafruit_LSM303.LSM303()
 

#lsm303 = Adafruit_LSM303.LSM303(busum=2)
 
print('Printing accelerometer & magnetometer...')
filename = "launchdata_"+str(datetime.datetime.now())+".txt"
file = open(filename, "w+")
for i in range (0, 250):
    # Read the X, Y, Z axis acceleration values and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out
    accel_x, accel_y, accel_z = accel
    mag_x, mag_z, mag_y = mag
    file.write('Accel X={0}, Accel Y={1}, Accel Z={2}\n'.format(round(accel_x/105.0,2), round(accel_y/105.0, 2), round(accel_z/105.0, 2)))
    print('Accel X={0}, Accel Y={1}, Accel Z={2}'.format(accel_x, accel_y, accel_z)) 
    file.write('Total Accel =' + math.sqrt(math.pow(round(accel_x/105.0,2),2) + math.pow(round(accel_y/105.0, 2),2)+ math.pow(round(accel_z/105.0, 2),2))
    print('Total Accel =' + math.sqrt(math.pow(round(accel_x/105.0,2),2) + math.pow(round(accel_y/105.0, 2),2)+ math.pow(round(accel_z/105.0, 2),2))
    # Wait half a second and repeat.
    time.sleep(0.5)
    #upload data to seperate file since no screen
file.close()