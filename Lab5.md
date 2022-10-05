# Lab 5

1. Write a python function `rollAdice`. The function receives the number of faces of a dice and returns the value once the dice is rolled. Assume the number received by the function is a positive integer value. Your function makes use of the `Random` module.

2. Write a python program `Lab5-1.py` that:
   - Prompt the user for the number of faces of the dice.
   - Validates the number of faces as an integer (use `try except` and a `while` loop)
   -  On the Sense HAT, turn on as many leds as the number of faces. Use the color of your choice.


3. Write a python function `displayColorForTemperature` ,
   The function receives a `float` value as an argument representing a temperature in Celsius.
   Depending on the temperature range, the following colors will be displayed on the Sense HAT

   | **-40c to -10c** | **dark blue**   |
   | ---------------- | --------------- |
   | **-9c to 0c**    | **blue**        |
   | **1c to 15c**    | **light green** |
   | **16c to 22c**   | **green**       |
   | **22c**          | **red**         |

4. Write a python function `LedsOnForHumidity` ,
   The function receives an integer value as an argument representing the humidity as a percentage
   Depending on the humidity range, the Sense HAT displays the relative number of blue lines (100% will be all leds sets to blue)
5. Based on the code of the main program of the "Sense HAT Sensors Display" available at this link: https://trinket.io/sense-hat write the code to test your two functions `displayColorForTemperature` and `LedsOnForHumidity`. Save the program as `Lab5-2.py`
6. Test your 2 programs both online ( https://trinket.io/sense-hat ) and on the Pi using the Sense Hat emulator.
7. Upload your 2 programs on GitHub.

