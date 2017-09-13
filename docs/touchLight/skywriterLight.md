<h1 align = "center"> Project: Touch Light </h1>
<p align = "center"> Mentor Guide</p>


<img src="./media/skywriter.png">

### Description
In this project we are going to combine the <a href = "https://thepihut.com/products/skywriter-hat">Skywriter HAT</a> with IKEA's TRÅDFRI smart lights to create a touch remote out of the Raspberry Pi.


### Goals
We want to write code that:
  - Let's us turn the TRÅDFRI light on and off by tapping the skywriter.
  - Changes the colour of the TRÅDFRI light by flicking the skywriter.
  - Changes the brightness of the TRÅDFRI light by moving our hand up.


### Manual

To complete this project, students will be working with a Go4Code Mentor writing code in python using IDLE and the command-line to control the Raspberry Pi.

***Note: Use Python 2.7 (IDLE2)***

### Concepts

The point of this task is to teach control flow and to show how programming can allow us to control electronics.

First we introduce the students to the python functions that can control the lights and then bring it together to create the program.

#### Using the lights
***Mac/Linux Demo***

We'll be using go4code python wrappers to control our lights.

If you haven't already, download the smartLightFolder into an appropriate directory using the following command:

```
git clone  
```

* Open IDLE2 and create a new file.
* Use the code below to import the tradfriLight library.
```
from tradfriLight import *
```
* The functions below can be used to control the light.

##### Functions

**Turn Light On**
```
turnLightOn()
```

**Turn Light Off**
```
turnLightOff()
```

**Set brightness**
```
setBrightness(0.7) ## Takes brightness as a percentage
```
**Set Colour**
The colourNumbers are 0 for 'cold', 1 for 'normal', 2 for 'warm'
```
setColour(colourNumber) #takes an integer between 0 and 2.
```

##### Control flow

The functions below can be used along with if-elif-else statements to create the appropriate control flow needed to use the skywriter as a remote for the light.

**Check if On**

Function returns True if the light is on and False if off.

```
isOn()
```
**Check if Tapped**
Function returns True if the skywriter has been tapped.

```
was_tapped()
```

**Check if Flicked**

Function returns True if the skywriter has been flicked.

```python
was_flicked()
```

**Get the Height**

Function returns the vertical distance between the skywriter and users hand.

```python
get_height()
```


**Creating a toggle**
*This section contains a guide on explaining control flow and a model solution*

<img src = "./media/controlFlow.png">

The code below will create a toggle switch for the light using the skywriter.

```
while True:
    if was_tapped():
        if isOn():
            turnLightOff()
        else:
            turnLightOn()

```
**Changing colour**

*This code alone just switches the light colour if it is on. This is to be used in combination with other code.*

```
while True:
  if isOn():
    if was_flicked:
        changeColour()
```


**Changing brightness**
