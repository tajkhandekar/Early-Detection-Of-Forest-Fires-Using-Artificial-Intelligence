import board
import adafruit_scd30
import time
import urllib.request
from MQ import *

sensor = adafruit_scd30.SCD30(board.I2C())
seconds = 0
baseURL = 'http://api.thingspeak.com/update?api_key=PRL0OA2YY2D2AEKB'
mq = MQ()
carbonm = mq.MQPercentage()

while seconds < 300:
    if type(seconds/15) == int:
        print("CO2 ppm: " + str(sensor.CO2))
        print("CO ppm: " + str(carbonm["CO"]*100))
        print("Temperature: " + str(sensor.temperature))
        print("Humidity: " + str(sensor.relative_humidity))
        print("Time Passed: " + str(seconds) + " seconds")
    f = urllib.request.urlopen(baseURL + '&field1=' + str(seconds) + '&field2=' + str(sensor.CO2) + '&field3=' + str(carbonm["CO"]*100) + '&field4=' + str(sensor.temperature) + '&field5=' + str(sensor.relative_humidity))
    f.read()
    f.close()
    seconds += 1
    time.sleep(1)
print("Done")