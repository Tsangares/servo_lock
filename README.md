## Context

This tool is showcased in the project [IotaWorkshop](https://github.com/Tsangares/iotaworkshop)

# Summary

This tool can be both used as a command line interface or be imported into your project. What this repo has that others do not is some math to calculate the estimated time it takes to rotate the servo to a sepecific destination. The utility handles all the pin IO and all you have to do is specify the location the servo needs to be in and the library will do the rest.

# Installation

This project requires `RPi.GPIO`, and I installed it using the arch repo using,

    yay -S python-raspberry-gpio
	
But ubuntu or rasbian can use,

    pip install RPi.GPIO

To install the servo library simply pull from the pip repo,

    pip install servo-lock
	
# Command Line Interface Examples

To send the servo to a sepecific location simply use the command

    servo move 19 90 #Moves the servo on pin 19 to 90 degrees



