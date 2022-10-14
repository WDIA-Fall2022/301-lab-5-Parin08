from sense_hat import SenseHat
import time

s = SenseHat()


# This function will return specific color according to temprature
def displayColorForTemperature(temp):
    if -40 <= temp <= -10:
        return (0, 0, 155)
    elif -9 <= temp <= 0:
        return (0, 0, 255)
    elif 1 <= temp <= 15:
        return (144,238,144)
    elif 16 <= temp < 22:
        return (0, 255, 0)
    elif temp >= 22:
        return (255, 0, 0)


# This function will turn on appropriate ammount of LEDs(if above 87.5 then all rows of leds on,if less then 12.5 then only 1 line of leds )
# This function will take 2 args temprature and humidity
def LedsOnForHumidity(hum,temp):
    num = hum / 12.5
    i = 0
    j = 0
    while (i < num):
        while (j < 8):
            # Calling displayColorForTemperature() to get proper color
            s.set_pixel(j, i, displayColorForTemperature(temp))
            if (j == 7):
                j = 0
                break
            j += 1

        i += 1

choice = 1

while(choice!=0):
    try:
        temp = int(input("Please enter temprature between -40 to 22."))
        hum = int(input("Please enter humidity between 0 to 100."))

        if((temp<-41 or temp>23) or (hum<0 or hum>100) ):
            print("Please enter values within provides range")
        else:
            LedsOnForHumidity(hum,temp)
        choice = int(input("Do you want to quit then press 0."))

    except:
        print("Not valid inputs please try again.")







